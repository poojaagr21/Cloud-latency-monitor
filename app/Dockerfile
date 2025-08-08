# ➊ Base image
FROM python:3.11-slim

# ➋ Install dependency (only Flask here)
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ➌ Copy your source code
COPY app.py .

# ➍ Runtime config
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "app.py"]