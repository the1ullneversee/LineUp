import React, {useState, useEffect } from 'react';
import {useParams} from 'react-router-dom';
import { Link } from 'react-router-dom';

const User = () => {

    //get the id from the url params
    const { id } = useParams();


    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [user, getUser] = useState([]);

    //allows us to call the backend to get the user data!
    useEffect(() => {
        fetch("http://127.0.0.1:8000/user/?user_id="+id)
            .then(res => res.json())
            .then(
                (data) => {
                    console.log(data);
                    getUser(data);
                    setIsLoaded(true);
                },
                (error) => {
                    setIsLoaded(true)
                    setError(error);
                }
            )
    }, [])

    if (error) {
        return <div>Error: {error.message}</div>;
    }
    if (!isLoaded) {
        return <div> Loading...</div>;
    }
    if (user) {
        return (
            <div>
                
                <h1>{user.first_name}, {user.last_name}</h1>
                <p>{user.email}</p>

                <div>
                    <img src={user.avatar}></img>
                    
                </div>
                <Link to={`/`}>Home</Link>
            </div>
        )
    }
}

export default User;