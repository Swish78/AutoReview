// src/components/About.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const About = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/api/about/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.error('There was an error fetching the about data!', error);
            });
    }, []);

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
            <h1 className="text-4xl font-bold mb-4">About Page</h1>
            <p className="text-lg text-gray-700">{message}</p>
        </div>
    );
};

export default About;
