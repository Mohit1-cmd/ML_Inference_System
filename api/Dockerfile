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

#Copies everything from api/ → /app
#This happens after installing dependencies to avoid reinstalling every time code changes
COPY api/ .

#Sets the default command to run when the container starts
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]