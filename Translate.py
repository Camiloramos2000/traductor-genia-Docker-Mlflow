from model import Model
import mlflow
import hashlib
import os

class Translater:
    def __init__(self):
        self.text = None
        self.target_language = None

    def translate(self, text, target_language):
        self.text = text
        self.target_language = target_language

        prompt = f"Translate the following text to {self.target_language}: {self.text}"

        # MLflow server (nombre del contenedor si corre en Docker)
        mlflow.set_tracking_uri(os.getenv("MLFLOW_URI", "http://mlflow-server:5000"))
        mlflow.set_experiment("traduccion_genai")

        prompt_hash = hashlib.md5(prompt.encode()).hexdigest()[:8]

        translated_text, len_answer, time_inferenced = Model.use(prompt)
        latency_ms = time_inferenced * 1000.0

        # Registrar run en MLflow
        with mlflow.start_run(run_name=f"traduccion_{prompt_hash}"):
            mlflow.log_param("idioma_objetivo", target_language)
            mlflow.log_param("modelo", "gemini-2.5-flash")
            mlflow.log_param("lenguaje_origen", "auto")
            mlflow.log_param("prompt_hash", prompt_hash)

            mlflow.log_metric("latency_ms", latency_ms)
            mlflow.log_metric("len_response", len_answer)

            # guardar artifact
            os.makedirs("/tmp/artifacts", exist_ok=True)
            artifact_path = f"/tmp/artifacts/traduccion_{prompt_hash}.txt"
            with open(artifact_path, "w", encoding="utf-8") as f:
                f.write(f"ORIGINAL:\n{text}\n\nTRADUCCIÓN:\n{translated_text}")
            mlflow.log_artifact(artifact_path)

        return translated_text, f"{latency_ms:.2f} ms"
