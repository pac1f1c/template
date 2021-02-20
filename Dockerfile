FROM python:3
ADD quine.py /
CMD [ "python", "./quine.py" ]
