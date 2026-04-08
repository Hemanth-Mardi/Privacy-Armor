FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir openenv-core pydantic uvicorn fastapi requests

# Copy all files from your repo to the container
COPY . .

# Expose the mandatory Hugging Face port
EXPOSE 7860

# Command to start your FastAPI app from app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
