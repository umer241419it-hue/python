"""
INSTRUCTIONS TO RUN THIS CODE:

1. Add your images to the 'faces' folder.
2. Change the image paths in the code to match your file locations,
   or rename your images to person1.jpg, person2.jpg, person3.jpg, and so on.
3. Update the corresponding names in the code to match each image.
4. You can add as many images as you want - just make sure to:
   - Add the correct path for each new image in the code
   - Add the corresponding name for each new image in the code
"""

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

person1_image = face_recognition.load_image_file(r"C:\Users\kadiw\OneDrive\Desktop\Python\FaceRecognition_Attendence\faces\person1.jpg")
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]
person2_image = face_recognition.load_image_file(r"C:\Users\kadiw\OneDrive\Desktop\Python\FaceRecognition_Attendence\faces\person2.jpg")
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]
person3_image = face_recognition.load_image_file(r"C:\Users\kadiw\OneDrive\Desktop\Python\FaceRecognition_Attendence\faces\person3.jpg")
person3_face_encoding = face_recognition.face_encodings(person3_image)[0]

known_face_encodings = [person1_face_encoding, person2_face_encoding, person3_face_encoding]
known_face_names = ["Person 1", "Person 2", "Person 3"]

students = known_face_names.copy()

face_locations = []
face_encodings = []

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "a+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        name = "Unknown"

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, date_str, time_str, "Present"])


    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()