# Traductor GenAI con Docker y MLflow

## Descripción

Esta aplicación permite traducir texto a distintos idiomas usando un modelo generativo (GenAI) a través del SDK compatible (Google Gemini). Cada interacción se registra en un servidor **MLflow Tracking** para llevar métricas como latencia, longitud de respuesta y artifacts de traducción.

La aplicación se ejecuta en **contenedores Docker** separados: uno para la app y otro para MLflow, sin usar `docker-compose`. Se puede publicar en Docker Hub y ejecutar remotamente pasando la API key por variable de entorno.

---

## Estructura del proyecto

```
traductor-app/
├─ main.py            # Interfaz Gradio
├─ Translate.py       # Lógica de traducción + MLflow
├─ model.py           # Clase Model para llamar a GenAI
├─ requirements.txt   # Dependencias Python
├─ Dockerfile         # Dockerfile de la app
├─ mlruns/            # Carpeta opcional para persistencia MLflow
```

---

## Requisitos

- Docker
- Python 3.11 (para desarrollo local)
- API Key de Google GenAI
- Puerto 7860 libre para Gradio

---

## Instalación y ejecución local (opcional)

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la app:

```bash
export GENAI_API_KEY="TU_API_KEY"
export MLFLOW_URI="http://localhost:5000"
python main.py
```

3. Abrir Gradio en `http://localhost:7860` y probar traducciones.

---

## Levantar servidor MLflow en Docker

1. Crear red Docker:

```bash
docker network create traductor-net
```

2. Ejecutar contenedor MLflow:

```bash
docker run -d --name mlflow-server \
  --network traductor-net \
  -p 5000:5000 \
  -v $(pwd)/mlruns:/mlruns \
  mlflow/mlflow:2.7.1 mlflow server \
  --backend-store-uri /mlruns \
  --default-artifact-root /mlruns \
  --host 0.0.0.0 --port 5000
```

- UI MLflow: `http://localhost:5000`

---

## Dockerizar y ejecutar la app

1. Construir imagen:

```bash
docker build -t tu_usuario/traductor-genai:1.0.0 .
```

2. Ejecutar la app:

```bash
docker run --rm -p 7860:7860 \
  --network traductor-net \
  -e GENAI_API_KEY="TU_API_KEY" \
  -e GRADIO_SERVER_PORT=7860 \
  -e MLFLOW_URI="http://mlflow-server:5000" \
  tu_usuario/traductor-genai:1.0.0
```

- Abrir Gradio en `http://localhost:7860`
- Cada traducción queda registrada en MLflow.

---

## Publicar imagen en Docker Hub

1. Login:

```bash
docker login
```

2. Taggear la imagen:

```bash
docker tag tu_usuario/traductor-genai:1.0.0 tu_usuario/traductor-genai:1.0.0
```

3. Subir a Docker Hub:

```bash
docker push tu_usuario/traductor-genai:1.0.0
```

---

## Ejecutar la app en otra máquina

```bash
docker pull tu_usuario/traductor-genai:1.0.0

docker run --rm -p 7860:7860 \
  --network traductor-net \
  -e GENAI_API_KEY="TU_API_KEY_REMOTA" \
  -e GRADIO_SERVER_PORT=7860 \
  -e MLFLOW_URI="http://<IP_servidor_MLflow>:5000" \
  tu_usuario/traductor-genai:1.0.0
```

- La app se conecta al servidor MLflow remoto y registra todos los runs.

---

## Variables de entorno importantes

- `GENAI_API_KEY`: clave de tu cuenta GenAI.  
- `GRADIO_SERVER_PORT`: puerto de la interfaz Gradio (default: 7860).  
- `MLFLOW_URI`: URL del servidor MLflow (puede ser contenedor Docker o remoto).

---

## Observaciones

- No incluir la API key dentro de la imagen o el repositorio.  
- Latencia y longitud de la respuesta se registran automáticamente en MLflow.  
- Mantener la red Docker `traductor-net` para que app y MLflow se comuniquen correctamente.

---

## Capturas de pantalla (entregables)

1. Traducción generada en Gradio.  
2. Run correspondiente en la UI de MLflow con métricas y artifact.

---

## Autor
camilo andres ramos cotes