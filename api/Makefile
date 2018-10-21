PROJECT_ID := $(shell gcloud config get-value project -q)

build:
	gcloud builds submit --config api_build.yaml .

pull:
	docker pull gcr.io/$(PROJECT_ID)/ceres-api:v1

start:
	docker run 	-it --rm  \
				-p 5000:8080 \
				gcr.io/$(PROJECT_ID)/ceres-api:v1
