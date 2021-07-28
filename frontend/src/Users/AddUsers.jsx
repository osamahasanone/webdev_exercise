import React, { useCallback } from "react";

const addUsersBulk = async () => {
  await fetch("http://127.0.0.1:5000/users", {
    method: "POST",
  });
};

export function AddUsers({ refetch }) {
  const onClick = useCallback(() => {
    addUsersBulk().then(refetch);
  }, [refetch]);
  return <button onClick={onClick}>Add Users</button>;
}

const addSkillsBulk = async () => {
  await fetch("http://127.0.0.1:5000/skills", {
    method: "POST",
  });
};

export function AddSkills({ refetch }) {
  const onClick = useCallback(() => {
    addSkillsBulk().then(refetch);
  }, [refetch]);
  return <button onClick={onClick}>Add Skills</button>;
}
