build:
	gcloud builds submit --config api_build.yaml .

start:
	docker run 	-it --rm  \
				-p 5000:5000 \
				-v /Users/victorr/webApplications/ceres/model/:/app/model \
				-v /Users/victorr/webApplications/ceres/api/:/app/ \
				gcr.io/ceres-219917/ceres-api:v1