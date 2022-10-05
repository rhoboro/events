FROM python:3.11.0rc2-slim
RUN apt update -y && apt upgrade -y && apt install -y binutils file gdb strace && apt-get clean
WORKDIR /app
CMD ["python3"]
