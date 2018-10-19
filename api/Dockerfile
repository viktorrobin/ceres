FROM ubuntu:16.04

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install vim make git python-pip

COPY . /app
WORKDIR /app

# Update pip and install flask
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["ceres_api.py"]