import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { GoogleOAuthProvider } from "@react-oauth/google";

ReactDOM.createRoot(document.getElementById("root")).render(
  <GoogleOAuthProvider clientId="610235815418-0fvbqdavt818260kjn53kguqo55fpkhf.apps.googleusercontent.com">
    <App />
  </GoogleOAuthProvider>
);
