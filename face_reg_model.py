import face_recognition
import glob
import re #regex
#image paths
image = glob.glob('known/*.jpg')

#images encodings
existing_images = [face_recognition.load_image_file(img) for img in glob.glob('known/*.jpg')]

#names of people in the images
names = [re.findall(r'\w+',name)[-2] for name in image]
#image encodings
existing_enc = [face_recognition.face_encodings(img)[0] for img in existing_images] 
#take a look!!
#image
#existing_images
names
#existing_enc
#loading the test image


test_image = face_recognition.load_image_file('images/elsisi2.jpg')

#encoding the test image
test_enc = face_recognition.face_encodings(test_image)
#comparing with the existing images

i = 0
for enc in existing_enc:
    #print (face_recognition.compare_faces(enc, test_enc))
    if(face_recognition.compare_faces(enc, test_enc)[0]):
        print("The image has %s in it." % (names[i]))
    i += 1