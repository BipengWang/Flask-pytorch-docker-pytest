# Flask-pytorch-docker-pytest
This is a Flask API on a docker container that accepts an API request of an Image and returns a list of class predictions. The API is tested by pytest.

The detailed information of pretrained resnet50 model could be found at https://github.com/NVIDIA/DeepLearningExamples and already implemented in this Flask API. A simple picture of golden retriever is provided for testing purpose. For each image request from the user, a list of 5 most possible predictions with their possibilities is returned. To set up environment for this API, please follow the instruction.

## 1.Run docker command to create an image with:
Make sure you have **Docker Desktop** installed on your machine.
```
docker build -t api-torch .
```
On this building process which takes some time, the environment required for this API is set up.

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

## 3. Test the status of the API
Make sure the pytest package is installed on your machine. Go to the directory you place this repository and enter the command:
```
pytest
```
If the test passes successfully, you would see such info:
```
========================================= test session starts ==========================================
platform darwin -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0
rootdir: /Volumes/T7/HW/CSCI590/Flask-pytorch-docker-pytest
plugins: anyio-3.5.0
collected 1 item                                                                                       

test_api.py .                                                                                    [100%]

========================================== 1 passed in 0.21s ===========================================
```
The pytest function checks the status code (200 if success) and whether 5 classifications are returned or not. 








