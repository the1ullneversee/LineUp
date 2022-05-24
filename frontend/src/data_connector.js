import React, { useState, useEffect }  from 'react';
import { Link } from 'react-router-dom';

const DC = () => {
const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [users, setUsers] = useState([]);
    useEffect(() => {
        fetch("http://127.0.0.1:8000")
            .then(res => res.json())
            .then(
                (data) => {
                    setIsLoaded(true);
                    setUsers(data);
                },
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
      }, [])
if (error) {
        return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
        return <div>Loading...</div>;
    } else {
        return (
            <div><h1>User List</h1>
                <ul>
                    {users.map(user => (
                        <li key={user.id}>
                            <Link to={`user/${user.id}`}>{user.name}</Link>
                        </li>
                    ))}
                </ul>
            </div>
            // <ul>
            //     {users.map(user => (
            //     <li>
            //         <Link to={`user/${user.id}`}>{user.name}</Link>
            //     </li>
            //     ))}
            // </ul>
        );
    }
}
export default DC;