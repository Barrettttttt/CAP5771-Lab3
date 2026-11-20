FROM python:3-slim

WORKDIR /app

COPY binder/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY AB_NYC_2019.csv .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

