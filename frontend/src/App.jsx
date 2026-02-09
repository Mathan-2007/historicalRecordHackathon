import { useState } from "react";

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const uploadImage = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError("Backend not reachable");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h2>AI Handwritten Record Digitization</h2>

      <input type="file" accept="image/*" onChange={uploadImage} />

      {loading && <p>⏳ Processing… (OCR + 3 AI models)</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <>
          <h3>📜 OCR Text</h3>
          <pre>{result.ocr_text}</pre>

          <h3>🧠 LLaMA Output</h3>
          <pre>{result.llama}</pre>

          <h3>🧠 DeepSeek Output</h3>
          <pre>{result.deepseek}</pre>

          <h3>🧠 Qwen Output</h3>
          <pre>{result.qwen}</pre>

          <h2>✅ Final Consensus Output</h2>
          <pre style={{ background: "#f0f0f0", padding: 10 }}>
            {result.final_output}
          </pre>
        </>
      )}
    </div>
  );
}

export default App;
