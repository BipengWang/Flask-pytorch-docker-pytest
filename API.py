# import os
# os.environ[ 'MPLCONFIGDIR' ] = '/tmp/'
from flask import Flask, request, make_response, render_template, jsonify
# import requests
from PIL import Image
from werkzeug.utils import secure_filename
import random
from datetime import datetime
import os
import torch
import torchvision.transforms as transforms
# import validators
# import numpy as np
import warnings
warnings.filterwarnings('ignore')


device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
resnet50 = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_resnet50', pretrained=True)
utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_convnets_processing_utils')
resnet50.eval().to(device)


# def get_img_from_rui(uri):
#     if validators.url(uri):
#         img = Image.open(requests.get(uri, stream=True).raw)
#     else:
#         img = Image.open(uri)
#     return img


# def get_img_from_local(path):
#     img = Image.open(path).convert('RGB')
#     return img


def save_img(img):
    img_name = secure_filename(img.filename)
    random_num = random.randint(0, 100)
    print(img_name)
    img_name = datetime.now().strftime("%Y%m%d%H%M%S")+"_"+str(random_num)+'.'+img_name.rsplit('.', 1)[1]
    img_path = BASE_DIR + "/static/img/"
    if not os.path.exists(img_path):
        os.makedirs(img_path, 755)
    img.save(img_path + img_name)
    return img_path, img_name


def preprocess(img, cuda=False):
    img_transforms = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor()])
    img = img_transforms(img)
    with torch.no_grad():
        mean = torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1)
        img = img.float()
        if cuda:
            mean = mean.cuda()
            std = std.cuda()
            img = img.cuda()
        # print(img.shape)
        input_pred = img[:3, :, :].unsqueeze(0).sub_(mean).div_(std)
    return input_pred.to(device)


def predict(img_pil):
    img_pre = preprocess(img_pil)
    with torch.no_grad():
        output = torch.nn.functional.softmax(resnet50(img_pre), dim=1).to(device)
    results = utils.pick_n_best(predictions=output, n=5)
    return results[0]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
classification = ['1st class & Possibility', '2nd class & Possibility', '3rd class & Possibility',
                  '4th class & Possibility', '5th class & Possibility']
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_img():
    if request.method == 'GET':
        res = make_response(render_template('ImgPost.html'))
        return res
    else:
        if 'myImg' in request.files:
            img = request.files.get('myImg')
            img_path, img_name = save_img(img)
            img = Image.open(img)
            prediction = predict(img)
            predict_json = {}
            for i in range(5):
                predict_json.update({classification[i]: prediction[i]})
            return jsonify(predict_json)

        # elif 'myURL' in request.url:
        #     img = get_img_from_rui('myURL')
        #     img_path, img_name = save_img(img, 0, 'jpg')
        #     prediction = predict(img_path, img_name)
        #     return prediction
        else:
            return 'No Image Found'


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0', port=80, debug=True)
