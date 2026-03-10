import React, { useEffect, useState } from 'react';

const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

function Users() {
  const [data, setData] = useState([]);

  useEffect(() => {
    console.log('Fetching Users from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Fetched Users:', json);
      })
      .catch(err => console.error('Error fetching Users:', err));
  }, []);

  return (
    <div>
      <h3>Users</h3>
      <ul>
        {data.map((item, idx) => (
          <li key={item.id || idx}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
