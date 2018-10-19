# FROM tensorflow/tensorflow:1.12.0-rc0-devel-py3
# FROM ubuntu:18.04
FROM continuumio/anaconda:5.3.0

# Housekeeping and install git
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install vim make

# Update pip and install flask
# RUN pip install --upgrade pip && \
#     pip install Flask==1.0.2

# Install tensorflow from conda for better performance
RUN conda install --yes tensorflow && \
    conda install --yes -c conda-forge tensorflow-hub

# Download stuff related to     
# RUN mkdir /tensorflow
# WORKDIR /tensorflow

# RUN git clone https://github.com/tensorflow/hub.git && \
#     git pull
# RUN curl -LO https://github.com/tensorflow/hub/raw/master/examples/image_retraining/retrain.py

# WORKDIR /
# RUN git clone https://github.com/tensorflow/models.git && cd models \
#     git pull
    # pip install --user -r official/requirements.txt

# WORKDIR /
# RUN git clone https://github.com/tensorflow/tensorflow.git && cd tensorflow \
#     git pull
    # pip install --user -r official/requirements.txt


# CMD ["/bin/bash"]