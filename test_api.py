import requests
import json


def test_api():
    img = open('/Users/bipengwang/Desktop/Golden_Retriever_from_baidu.jpg', 'rb')
    files = {'myImg': img}
    r = requests.post('http://127.0.0.1:80/', files=files)
    result = r.text
    result_json = json.loads(result)
    classification = ['1st class & Possibility', '2nd class & Possibility', '3rd class & Possibility',
                      '4th class & Possibility', '5th class & Possibility']
    assert r.status_code == 200
    assert result_json[classification[0]] == ['golden retriever', '79.1%']
    assert result_json[classification[1]] == ['collie', '0.7%']
    assert result_json[classification[2]] == ['kuvasz', '0.7%']
    assert result_json[classification[3]] == ['Pembroke, Pembroke Welsh corgi', '0.5%']
    assert result_json[classification[4]] == ['Labrador retriever', '0.5%']

