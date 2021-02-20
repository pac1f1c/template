FROM python:3
ADD guessit.py /
CMD [ "python", "./guessit.py" ]