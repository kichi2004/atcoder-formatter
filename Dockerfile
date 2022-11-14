FROM python:3.10-bullseye

WORKDIR /app

RUN apt update && apt upgrade -y && \
    apt install clang-format -y && \
    pip install --upgrade pip
ADD https://dot.net/v1/dotnet-install.sh .
RUN chmod +x ./dotnet-install.sh && ./dotnet-install.sh
ENV PATH $PATH:/root/.dotnet
RUN dotnet tool install -g dotnet-format

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
