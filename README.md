---
title: Getaround Mlflow
emoji: 💻
colorFrom: pink
colorTo: pink
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# getaround

This project contains two services: MLflow and FastAPI, both deployed using Docker.

## Structure

- `mlflow/`: Contains the MLflow server configuration and Dockerfile.
- `fastapi/`: Contains the FastAPI application and Dockerfile.
- `docker-compose.yml`: Orchestrates the deployment of both services.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/nprevost/getaround.git
   cd getaround
