# Your Solution
FROM python:3.9
WORKDIR /usr/src/app
COPY ./app /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
CMD python -m uvicorn main:app --host 0.0.0.0 --port 4000