import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('/api/home/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.error('There was an error fetching the home data!', error);
            });
    }, []);

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
            <h1 className="text-4xl font-bold mb-4">Home Page</h1>
            <p className="text-lg text-gray-700">{message}</p>
        </div>
    );
};

export default Home;