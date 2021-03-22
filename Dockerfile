FROM python:3

ADD Source /Source/

CMD [ "python", "Source/calc_test.py" ]