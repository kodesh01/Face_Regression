
import cv2
from face2 import SimpleFacerec
import pyttsx3
# initialize Text-to-speech engine.
engine = pyttsx3.init()

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("/home/kodesh/Documents/ img/")

# Load Camera
cap = cv2.VideoCapture(0)

text = "Face  Detection ACTIVITED "
engine.say(text)
engine.runAndWait()

while True:
    ret, frame = cap.read()


    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):

        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        text = "Face  Detected"
        engine.say(text)
        engine.runAndWait()



    cv2.imshow("Frame", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

