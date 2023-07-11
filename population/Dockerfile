FROM python:3.10

WORKDIR /population
COPY requirements.txt /population/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /population/requirements.txt

COPY . /population

CMD bash -c "while true; do sleep 1; done"