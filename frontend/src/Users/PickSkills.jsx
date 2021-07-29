import React, { Component } from "react";
import "antd/dist/antd.css";
import { Select } from "antd";
const { Option } = Select;

class PickSkills extends Component {
  handleChange = async (value) => {
    await fetch(`http://127.0.0.1:5000/users/${this.props.user.id}/setskills`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skills: value }),
    }).then(this.props.refetch);
  };

  render() {
    return (
      <Select
        mode="tags"
        style={{ width: "100%" }}
        placeholder="pick skills or type to create.."
        defaultValue={this.props.user.skills.map((skill) => skill.name)}
        onChange={this.handleChange}
      >
        {this.props.allSkills.map((skill) => (
          <Option key={skill.name}>{skill.name}</Option>
        ))}
      </Select>
    );
  }
}

export default PickSkills;
