import React, { useCallback } from "react";

const addUsersBulk = async () => {
  await fetch("http://127.0.0.1:5000/users", {
    method: "POST",
  });
};

export default function AddUsers({ refetch }) {
  const onClick = useCallback(() => {
    addUsersBulk().then(refetch);
  }, [refetch]);
  return <button onClick={onClick}>Add Users</button>;
}
