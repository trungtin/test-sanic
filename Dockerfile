FROM python:3.11-slim

WORKDIR /sanic

ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
        gcc g++ libffi-dev build-essential git-all
        # \
    # && apt-get autoremove --yes gcc g++ libffi-dev build-essential \
    # && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]