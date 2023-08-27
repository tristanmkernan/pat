FROM python:3.10-slim

ARG LITESTREAM_PLATFORM=arm64

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# RUN apt-get update
# RUN apt-get install -y \
#     libmagic-dev \
#     libjpeg-dev \
#     zlib1g-dev \
#     libffi-dev \
#     gfortran \
#     libopenblas-dev

COPY requirements.txt /code/

RUN pip install -r requirements.txt

# Download the static build of Litestream directly into the path & make it executable.
ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.11/litestream-v0.3.11-linux-${LITESTREAM_PLATFORM}.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz

# Copy Litestream configuration file & startup script.
COPY litestream.yml /etc/litestream.yml

COPY . /code/

COPY .env.prod .env

RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]

ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
