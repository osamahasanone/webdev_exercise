import React, { Component } from "react";
import "antd/dist/antd.css";
import { Select } from "antd";

const { Option } = Select;

class SearchUsers extends Component {
  onChange = async (value) => {
    await fetch(
      `http://127.0.0.1:5000/userswithskill?skill_name=${encodeURIComponent(
        value
      )}`
    )
      .then((response) => response.json())
      .then((responseData) => this.props.setUsers(responseData.items));
  };

  render() {
    return (
      <div className="search">
        <h4>Search by skill:</h4>
        <Select
          showSearch
          style={{ width: 200 }}
          placeholder="Select a skill"
          optionFilterProp="children"
          onChange={this.onChange}
          filterOption={(input, option) =>
            option.props.children.toLowerCase().indexOf(input.toLowerCase()) >=
            0
          }
        >
          {this.props.allSkills.map((skill) => (
            <Option key={skill.name}>{skill.name}</Option>
          ))}
        </Select>
      </div>
    );
  }
}

export default SearchUsers;
