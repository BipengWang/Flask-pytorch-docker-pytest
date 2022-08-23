# Flask-pytorch-docker-pytest
This is a Flask API on a docker container that accepts an API request of an Image and returns a list of class predictions. The API is tested by pytest.
The detailed information of pretrained resnet50 model could be found at https://github.com/NVIDIA/DeepLearningExamples and already implemented in the flask. A simple 

## 1.Run docker command to create an image with:
```
docker build -t api-torch . #-t image name
```

## 2. Run image in a docker container with:
```
docker run -dp 80:80 --name api-torch api-torch 
```
Now you can go the address http://localhost:80/ on your browser and see a simple web with file submitting portal.





