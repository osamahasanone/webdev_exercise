import React, { Component } from "react";
import "antd/dist/antd.css";
import { Select } from "antd";
const { Option } = Select;

class UserSkill extends Component {
  state = {
    skills: [],
  };

  async componentDidMount() {
    const response = await fetch("http://127.0.0.1:5000/skills");
    const { items } = await response.json();
    this.setState({ skills: items });
  }

  handleChange = (value) => {
    console.log(`selected ${value}`);
  };

  render() {
    return (
      <Select
        mode="tags"
        style={{ width: "100%" }}
        placeholder="Choose Skills"
        defaultValue={["Python", "Flask"]}
        onChange={this.handleChange}
      >
        {this.state.skills.map((skill) => (
          <Option key={skill.name}>{skill.name}</Option>
        ))}
      </Select>
    );
  }
}

export default UserSkill;
