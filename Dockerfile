FROM python:3.7.3

WORKDIR /code

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# CMD ["bash"]
ENTRYPOINT [ "python", "app/jerk.py"]