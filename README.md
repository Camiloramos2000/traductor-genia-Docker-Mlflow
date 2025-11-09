<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF6F00?style=for-the-badge&logo=gradio&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Google GenAI](https://img.shields.io/badge/GenAI-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

<br/>

<div align="center">
  
# 🌐 Traductor Inteligente con Seguimiento en MLflow + Despliegue en Docker  
✨ *Interfaz Gradio + Registro Automático de Métricas y Artefactos*

</div>

---

### 🚀 Descripción General

Este proyecto implementa un **traductor con inteligencia generativa (Gen-AI)**, accesible desde una interfaz web construida con **Gradio**.  
Cada traducción realizada queda registrada automáticamente en **MLflow** (parámetros, métricas y artefactos), lo que permite monitorear el comportamiento del modelo y comparar ejecuciones.

El sistema está **contenedorizado completamente con Docker**, lo cual asegura portabilidad y despliegue reproducible en cualquier equipo.

---

## 🎨 Vista General del Proyecto

| Componente | Tecnología | Rol |
|----------|------------|-----|
| Interfaz Web | Gradio | Entrada y visualización de traducción |
| Modelo de Traducción | Gen-AI (Google) | Procesamiento y generación |
| Tracking Experimentos | MLflow | Registro de params, métricas y artefactos |
| Despliegue | Docker | Portabilidad y ejecución estándar |

---

## 🖼️ Evidencias Visuales

### 🌍 Interfaz del Traductor
<img src="img/interface_traductor.png" width="600">

### 📊 Panel de Métricas en MLflow

| Tipo | Vista |
|------|------|
| **Parámetros (Params)** | <img src="img/mlflow_parameter.png" width="600"> |
| **Métricas (Metrics)** | <img src="img/mlflow_metrics.png" width="600"> |
| **Artefactos (Artifacts)** | <img src="img/mlflow_artifacts.png" width="600"> |

---

## 🧱 Arquitectura del Sistema (Diagrama)

```mermaid
flowchart TD
    A[Usuario 💻] --> B[Interfaz Gradio 🌐]
    B --> C[Modelo Gen-AI 🤖]
    C --> D[(MLflow Tracking 📊)]
    D --> E[Parámetros]
    D --> F[Métricas]
    D --> G[Artefactos]

---

## 🐳 Ejecución con Docker

### 1. Crear network y volúmenes

```bash
docker network create translation-net
docker volume create mlflow_data
docker volume create mlflow_artifacts
```

### 2. Ejecutar el Traductor (desde Docker Hub)
Traemos la imagen del DockerHub:
#### camiloramos2000/traductor-genai:1.0.0 en DockerHub
<img src="img/imagen_app_dockerHub.png" width="600">

```bash
docker pull camiloramos2000/traductor-genai:1.0.0
```

> Reemplazar `TU_API_KEY` con tu API real.

```bash
docker run -it -d   --name traductor-genai   -p 7860:7860   --network translation-net   -e MLFLOW_URI="http://mlflow:5000"   -e GENAI_API_KEY="TU_API_KEY"   camiloramos2000/traductor-genai:1.0.0
```
Acceso interfaz Gradio:  
👉 http://localhost:7860

### 3. Ejecutar el servidor MLflow
traemos la imagen de DockerHub:

```bash
docker pull ghcr.io/mlflow/mlflow
```

```bash
docker run -d -it --rm   --name mlflow   --network translation-net   -p 5000:5000   -v mlflow_data:/mlflow   -v mlflow_artifacts:/mlflow/artifacts   mlflow   mlflow server     --backend-store-uri sqlite:////mlflow/mlflow.db     --default-artifact-root /mlflow/artifacts     --host 0.0.0.0     --port 5000
```
Acceso MLflow:  
👉 http://localhost:5000

---

## 💡 Funcionamiento Interno

- Cada traducción genera:
  - **Parámetros:** idioma destino, longitud del texto
  - **Métricas:** tiempo de traducción, conteo de tokens
  - **Artefactos:** logs e historial de traducciones

- Esto permite comparar versiones del modelo, rendimiento y calidad.

---

## 🏁 Conclusiones

| Componente | Estado |
|----------|:------:|
| Traductor Gen-AI | ✅ |
| Interfaz Gradio | ✅ |
| Tracking con MLflow | ✅ |
| Contenerización con Docker | ✅ |
| Reproducibilidad completa | ✅ |

---

## 👨‍💻 Autor

**Camilo Andrés Ramos Cotes (CRC)**  
Universidad del Magdalena  
GitHub: https://github.com/camiloramos2000
