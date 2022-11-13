FROM python:3.10-bullseye

WORKDIR /app

RUN apt update && apt upgrade -y && apt install clang-format -y && pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
