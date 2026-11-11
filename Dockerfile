#Using python 3.11 base image
FROM python:3.12-slim

#Set working directory
WORKDIR /main

#Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest of application code
COPY . .

#Expose the application port
EXPOSE 8001

#Comand to start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
