import React, { useCallback } from "react";
import { message } from "antd";

const success_notification = () => {
  message.success("Dummy Skills have been successfully added");
};

const error_notification = () => {
  message.error("Dummy Skills have already been added");
};

const addSkillsBulk = async () => {
  await fetch("http://127.0.0.1:5000/skills", {
    method: "POST",
  }).then(function (response) {
    if (!response.ok) {
      throw Error(response.statusText);
    }
    return response;
  });
};

export function AddSkills({ refetch }) {
  const onClick = useCallback(() => {
    addSkillsBulk()
      .catch(function (error) {
        error_notification();
      })
      .then(refetch)
      .then(function () {
        success_notification();
      });
  }, [refetch]);
  return <button onClick={onClick}>Add Skills</button>;
}
