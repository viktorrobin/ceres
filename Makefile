build-g:
	cd model
	gcloud builds submit --config model/conda_build.yaml .

build: 
	docker build \
		-t ceres:v1 \
		-f docker/dockerfile.api \
		.

start: 
	docker run -it \
		-v ~/webApplications/anubis/:/anubis \
		-p 5000:5000 \
		anubis:v1


dirModel := catDetector
nameModel := retrainedModel_$(shell date +%F_%H-%M-%S)
fullPathModel := $(dirModel)/$(nameModel)

retrain:
	mkdir $(dirModel)/$(nameModel)
	python $(dirModel)/retrain.py \
		--bottleneck_dir=$(fullPathModel) \
		--model_dir=$(fullPathModel) \
		--how_many_training_steps 10000 \
		--output_graph=$(fullPathModel)/retrained_graph.pb \
		--output_labels=$(fullPathModel)/retrained_labels.txt \
		--image_dir=$(dirModel)/data/training

# python label_image.py --graph=retrainedModel/retrained_graph.pb --labels=retrainedModel/retrained_labels.txt --input_layer=Placeholder --output_layer=final_result --image=validationPics/catEatingPlan.jpg