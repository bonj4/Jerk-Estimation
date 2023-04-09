FROM python:3.7-slim

WORKDIR /code

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app


ENV QT_X11_NO_MITSHM=1

# CMD [ "bash" ]

CMD [ "python", "app/jerk.py"]