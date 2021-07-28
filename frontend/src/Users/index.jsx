import { useCallback, useEffect, useState } from "react";
import { AddUsers, AddSkills } from "./AddUsers";
import UserSkill from "./UserSkills";
import RemoveUsers from "./RemoveUsers";
import "./Users.css";

const UsersTable = ({ children }) => (
  <div className="users-table">{children}</div>
);

const UsersTableHeader = () => (
  <div className="users-table__row">
    <div className="users-table__col-header">Id</div>
    <div className="users-table__col-header">Name</div>
    <div className="users-table__col-header">Skills</div>
  </div>
);

const UserRow = ({ id, name }) => (
  <div className="users-table__row">
    <div>{id}</div>
    <div>{name}</div>
    <div>
      <UserSkill />
    </div>
  </div>
);

const fetchUsers = async () => {
  const response = await fetch("http://127.0.0.1:5000/users");
  const { items } = await response.json();
  return items;
};

const UsersActions = ({ children }) => (
  <div className="users-actions">{children}</div>
);

export default function Users() {
  const [users, setUsers] = useState([]);
  const loadUsers = useCallback(() => {
    fetchUsers().then(setUsers);
  }, []);
  useEffect(loadUsers, [loadUsers]);
  return (
    <div>
      <UsersTable>
        <UsersTableHeader />
        {users.map((user) => (
          <UserRow key={user.id} {...user} />
        ))}
      </UsersTable>
      <UsersActions>
        <AddSkills />
        <AddUsers refetch={loadUsers} />
        <RemoveUsers refetch={loadUsers} />
      </UsersActions>
    </div>
  );
}
