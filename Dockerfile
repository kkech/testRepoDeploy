FROM python:3

ADD my_script.py /

RUN pip install flask

RUN export FLASK_APP=my_script.py
