FROM python:3.9

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python -m uvicorn main:app --reload