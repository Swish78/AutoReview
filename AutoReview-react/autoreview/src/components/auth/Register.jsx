import React from 'react';

const Register = () => {
    return (
        <div>
            <h1>Register</h1>
            <form>
                <div>
                    <label>Email:</label>
                    <input type="email" required />
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" required />
                </div>
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
