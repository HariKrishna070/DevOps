FROM python:3.12.10-slim
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG BACKEND_HOST_URL
ENV BACKEND_HOST_URL=${BACKEND_HOST_URL}

# Copy in the source code
COPY . .
EXPOSE 7860

CMD ["python3", "app.py"]