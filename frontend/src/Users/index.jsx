import { useCallback, useEffect, useState } from "react";
import AddUsers from "./AddUsers";

import PickSkills from "./PickSkills";
import SearchUser from "./search";
import RemoveUsers from "./RemoveUsers";
import "./Users.css";
import { Button, Tooltip } from "antd";
import { ReloadOutlined } from "@ant-design/icons";

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

const UserRow = ({ user, allSkills, refetch }) => (
  <div className="users-table__row">
    <div>{user.id}</div>
    <div>{user.name}</div>
    <div>
      <PickSkills allSkills={allSkills} refetch={refetch} user={user} />
    </div>
  </div>
);

const fetchUsers = async () => {
  const response = await fetch("http://127.0.0.1:5000/users");
  const { items } = await response.json();
  return items;
};

const fetchSkills = async () => {
  const response = await fetch("http://127.0.0.1:5000/skills");
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

  const [skills, setSkills] = useState([]);
  const loadSkills = useCallback(() => {
    fetchSkills().then(setSkills);
  }, []);
  useEffect(loadSkills, [loadSkills]);

  return (
    <div>
      {skills.length > 0 && (
        <SearchUser
          allSkills={skills}
          refetch={loadUsers}
          setUsers={setUsers}
        />
      )}
      <Tooltip title="Show all">
        <Button
          type="link"
          icon={<ReloadOutlined />}
          onClick={() => loadUsers()}
        >
          Show all
        </Button>
      </Tooltip>
      <UsersTable>
        <UsersTableHeader />

        {users.map((user) => (
          <UserRow
            allSkills={skills}
            refetch={loadSkills}
            key={user.id}
            user={user}
          />
        ))}
      </UsersTable>
      <UsersActions>
        <AddUsers refetch={loadUsers} />
        <RemoveUsers refetch={loadUsers} />
      </UsersActions>
    </div>
  );
}
