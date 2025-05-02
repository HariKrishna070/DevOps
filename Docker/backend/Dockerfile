FROM python:3.12.10-slim
WORKDIR /app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG MONGO_DB_USERNAME
ARG MONGO_DB_PASSWORD
ARG MONGO_URI

ENV MONGO_DB_USERNAME=${MONGO_DB_USERNAME} \
	MONGO_DB_PASSWORD=${MONGO_DB_PASSWORD} \
	MONGO_URI=${MONGO_URI}
	

# Copy in the source code
COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]