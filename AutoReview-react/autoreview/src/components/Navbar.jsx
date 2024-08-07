import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = ({ isAuthenticated, handleLogout }) => {
    return (
        <nav className="navbar">
            <Link to="/" className="navbar-brand">AutoReview</Link>
            <div className="navbar-links">
                {/*{isAuthenticated ? (*/}
                    <>
                        <Link to="/profile">Profile</Link>
                        <Link to="/about">About</Link>
                        <button onClick={handleLogout}>Logout</button>
                    </>
                {/*) : (*/}
                {/*    <>*/}
                {/*        <Link to="/login">Login</Link>*/}
                {/*        <Link to="/register">Register</Link>*/}
                {/*        <Link to="/about">About</Link>*/}
                {/*    </>*/}
                {/*)}*/}
            </div>
        </nav>
    );
};

export default Navbar;
