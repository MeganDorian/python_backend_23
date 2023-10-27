FROM python:3.11

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install poetry

ADD poetry.lock .
ADD pyproject.toml .

RUN poetry install

COPY /homework /homework

WORKDIR .
