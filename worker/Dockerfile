#Starting with a clean machine that already has Python installed
FROM python:3.10

#Sets /app as the current directory inside container
WORKDIR /app

#Copies requirements.txt from your local machine → container /app
#Why this separate step? -> Docker caching optimization (very important)
COPY requirements.txt .

#Install dependencies
#--no-cache-dir: Reduces image size (no pip cache stored)
RUN pip install --no-cache-dir -r requirements.txt

COPY worker/ .

CMD ["python", "worker.py"]