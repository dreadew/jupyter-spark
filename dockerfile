FROM python:3.11-slim

WORKDIR /home/jovyan

RUN apt-get update && \
    apt-get install -y curl git build-essential wget gnupg && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/share/man/man1 && \
    wget -O- https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /usr/share/keyrings/adoptium.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb bookworm main" | tee /etc/apt/sources.list.d/adoptium.list && \
    apt-get update && \
    apt-get install -y temurin-21-jdk && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY uv.lock pyproject.toml ./
COPY ./common ./common
COPY ./constants ./constants
COPY ./utils ./utils
COPY ./notebooks ./notebooks

RUN uv venv
RUN uv sync

COPY ./start_notebook.sh /start_notebook.sh
RUN chmod +x /start_notebook.sh

CMD ["/start_notebook.sh"]
