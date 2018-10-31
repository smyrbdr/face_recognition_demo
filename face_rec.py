!pip install face_recognition
!pip install dlib

import os
import face_recognition

images = os.listdir('images')
target_image = face_recognition.load_image_file('new_image.jpg')

target_image_encoded = face_recognition.face_encodings(target_image)[0]

for image in images:
    current_image = face_recognition.load_image_file("images/" + image)
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    
    result = face_recognition.compare_faces(
        [target_image_encoded], current_image_encoded)
   
    if result[0] == True:
        print "Matched: " + image
    else:
        print "Not matched: " + image
