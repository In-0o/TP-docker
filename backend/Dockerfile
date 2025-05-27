#Build
FROM python:3.9-slim AS BUILD
ENV TZ="Europe/Paris"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .


#run
FROM python:3.9-slim AS RUN
ENV TZ=Europe/Paris
RUN useradd -m appuser
WORKDIR /app
COPY --from=BUILD /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=BUILD /app .
RUN chown -R appuser:appuser /app
USER appuser
#EXPOSE 5000 est-ce que c'est mieux de l'exposer dnas le dockerfile ou docker compose ?
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python -c "import urllib.request; exit(0) if urllib.request.urlopen('http://localhost:5000').status == 200 else exit(1)" || exit 1