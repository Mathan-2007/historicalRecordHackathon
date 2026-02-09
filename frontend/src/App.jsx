import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";

function Admin() { return <h1>Admin Page</h1>; }
function Viewer() { return <h1>Viewer Page</h1>; }
function Verifier() { return <h1>Verifier Page</h1>; }

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/viewer" element={<Viewer />} />
        <Route path="/verifier" element={<Verifier />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
