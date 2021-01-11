import requests
import json

def test_face_match(image_path, person_name):
    url = 'http://127.0.0.1:5001/face_rec'
    # open file in binary mode
    binary_image = {'file': open(image_path , 'rb')}
    person_info  = {'person_name': person_name}     
    resp = requests.post(url, files=binary_image , data=person_info )
    print( 'face_match response:\n', json.dumps(resp.json()) )


if __name__ == '__main__':
    test_face_match('images/trudeau.jpg','Trudeau')