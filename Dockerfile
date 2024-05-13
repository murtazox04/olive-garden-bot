FROM python:3.10-alpine

WORKDIR /app

COPY . /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000", "--reload" ]