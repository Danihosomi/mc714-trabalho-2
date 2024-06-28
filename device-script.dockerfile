FROM python:3.11.5
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python", "./device.py"]
