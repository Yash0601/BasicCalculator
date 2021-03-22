FROM python:3

ADD src /Source

#RUN pip install pystrich

CMD [ "python", "./Source/calc_test.py" ]