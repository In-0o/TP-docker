FROM python:3.9-slim
# A COMPLETER
ENV TZ="Europe/Paris"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=30s --timeout=10s  --retries=3 CMD [ "CMD", "curl", "-f", "http://localhost:5000" ]