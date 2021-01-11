from flask import Flask, request
import os
import json
from face_rec_model import compare_recogenize

app = Flask(__name__)

@app.route('/face_rec', methods=['POST'])
def face_recognition():
    if request.method == 'POST':
        # new image name
        image_name = request.form['person_name'] + '.jpg'
        new_image_path = "new_images/" + image_name
        
        # check if the post request has the file part
        if 'file' in request.files:
            # save the new image into a directory 
            binary_image_req = request.files.get('file') 
           
            with open(new_image_path, 'wb') as f:
                f.write(binary_image_req.read())
                                     
            name = compare_recogenize(image_name)    
            resp_data = {'name': name }
            return json.dumps(resp_data)           
    
# When debug = True, code is reloaded on the fly while saved
app.run(host='0.0.0.0', port='5001', debug=True)
