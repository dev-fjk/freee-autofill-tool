import { Route, Routes } from "react-router-dom";

import ProjectsPage from "./pages/ProjectsPage";

function App() {
    return (
        <>
            <Routes>
                <Route path="/projects" element={<ProjectsPage />} />
                {/* 他のページを増やすならここに追加 */}
            </Routes>
        </>
    );
}

export default App;
