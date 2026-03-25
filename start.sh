#!/bin/bash

echo "Starting FastAPI..."
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

echo "Waiting for backend to start..."
sleep 5

echo "Starting Streamlit..."
streamlit run frontend/app.py --server.port 10000 --server.address 0.0.0.0