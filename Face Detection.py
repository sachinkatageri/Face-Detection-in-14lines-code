import cv2
face_cascade = cv2.CascadeClassifier(r'C:\Users\dell\Downloads\FaceDetect-master\FaceDetect-master\haarcascade_frontalface_default.xml')#haarcascade_path_location
cap = cv2.VideoCapture(0)# To capture video from webcam.
while True:
    _, img = cap.read() # Read the frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convert to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Detect the faces
    for (x, y, w, h) in faces:# Draw the rectangle around each face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) 
    cv2.imshow('img', img)# Display 
    k = cv2.waitKey(30) & 0xff# Stop if escape key is pressed
    if k==27:
        break
cap.release()# Release the VideoCapture object