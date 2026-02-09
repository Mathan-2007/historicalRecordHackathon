import { GoogleLogin } from "@react-oauth/google";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const handleLogin = async (credentialResponse) => {
    const token = credentialResponse.credential;

    const res = await axios.post("http://localhost:5000/auth/google", {
      token,
    });

    const { role } = res.data;

    if (role === "admin") navigate("/admin");
    if (role === "viewer") navigate("/viewer");
    if (role === "verifier") navigate("/verifier");
  };

  return (
    <div>
      <h2>Login</h2>
      <GoogleLogin onSuccess={handleLogin} onError={() => alert("Login Failed")} />
    </div>
  );
}

export default Login;
