import { useState, useEffect } from "react";
import { Route, Routes, Navigate } from "react-router-dom";

import ProjectsPage from "./pages/ProjectsPage";
import LoginPage from "./pages/LoginPage";

import { isLoggedIn } from "./utils/auth";

import Header from "./components/Header";
import UnAuthHeader from "./components/UnAuthHeader";

function App() {
    const [loggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        setLoggedIn(isLoggedIn());
    }, []);

    return (
        <>
            {loggedIn ? <Header /> : <UnAuthHeader />}
            <Routes>
                <Route
                    path="/"
                    element={loggedIn ? <Navigate to="/projects" replace /> : <Navigate to="/login" replace />}
                />
                <Route path="/login" element={<LoginPage onLogin={() => setLoggedIn(true)} />} />
                <Route path="/projects" element={<ProjectsPage />} />
            </Routes>
        </>
    );
}

export default App;
