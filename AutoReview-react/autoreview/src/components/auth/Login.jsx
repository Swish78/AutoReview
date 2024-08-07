import React from 'react';
import { useNavigate } from 'react-router-dom';

const Login = ({ handleLogin }) => {
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        // Perform login logic here
        handleLogin();
        navigate('/');
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Email:</label>
                    <input type="email" required />
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" required />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default Login;
