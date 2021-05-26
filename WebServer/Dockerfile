FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# prevent fork bombs
RUN bash -c "ulimit -S -u 100"

COPY . .

RUN useradd -ms /bin/bash web
USER web

CMD [ "python3", "__main__.py"]