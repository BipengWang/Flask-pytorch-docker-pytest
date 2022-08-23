# Flask-pytorch-docker-pytest
This is a Flask API on a docker container that accepts an API request of an Image and returns a list of class predictions. The API is tested by pytest.

The detailed information of pretrained resnet50 model could be found at https://github.com/NVIDIA/DeepLearningExamples and already implemented in this Flask API. A simple picture of golden retriever is provided for testing purpose. For each image request from the user, a list of 5 most possible predictions with their possibilities is returned. To set up environment for this API, please follow the instruction.

## 1.Run docker command to create an image with:
Make sure you have **Docker Desktop** installed on your machine.
```
docker build -t api-torch . #-t image name
```
On this building process, the environment required for this API is set up.

## 2. Run image in a docker container with:
```
docker run -dp 80:80 --name api-torch api-torch 
```
Now you can go the address http://localhost:80/ on your browser and see a simple web with file submitting portal. Submit the provided picture and you will get predictions like:
```
{
  "1st class & Possibility": [
    "golden retriever", 
    "79.1%"
  ], 
  "2nd class & Possibility": [
    "collie", 
    "0.7%"
  ], 
  "3rd class & Possibility": [
    "kuvasz", 
    "0.7%"
  ], 
  "4th class & Possibility": [
    "Pembroke, Pembroke Welsh corgi", 
    "0.5%"
  ], 
  "5th class & Possibility": [
    "Labrador retriever", 
    "0.5%"
  ]
}
```

To check, stop and remove containers and images, go with the commands:
```
docker ps
docker images
docker rm container-id
docker stop/start container-id
docker rmi image-id
```








