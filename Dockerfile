FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000