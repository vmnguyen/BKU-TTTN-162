import cv2




# Cascade path for face and eye detect 
imagePath = "abba.png"
facePath = "haarcascade_frontalface_default.xml"
eyePath = "haarcascade_eye.xml"
faceCasc = cv2.CascadeClassifier(facePath)
eyeCasc = cv2.CascadeClassifier(eyePath)

# Capture frames from camera
'''
cameraCapture = cv2.VideoCapture(0)
while True:
	_, frame = cameraCapture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	faceDetected = faceCasc.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (50, 50),
		flags = cv2.CASCADE_SCALE_IMAGE
	)
	for (x, y, w, h) in faceDetected:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
'''


cameraCapture = cv2.VideoCapture(0)
#Read image from path
image = cv2.imread(imagePath)
#Convert image to gray color
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
while True:
	_, image = cameraCapture.read()
	image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	faces = faceCasc.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (50, 50),
		flags = cv2.CASCADE_SCALE_IMAGE
		)

	for (x, y, w, h) in faces:
		#Draw a rectangle around the faces detected
		cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
		# for each face in list faces are detected, crop a rectangle of eyes
		eyesFrame = gray[y:y + 3*h/5,  x:x+w]
		# Detect eyes from a face
		eyes = eyeCasc.detectMultiScale(
				eyesFrame,
				scaleFactor = 1.06,
				minSize = (10,10),
				maxSize = (50, 50),
				minNeighbors = 3,
				#flags = cv2.CASCADE_SCALE_IMAGE
			)
		print "Found {0} eyes".format(len(eyes))
		for (xe, ye, we, he) in eyes:
			cv2.rectangle(image, (x + xe, y  + ye), (x + xe + we, y + ye + he), (0, 255, 0), 2)

		cv2.imshow('Detect face and eyes', image)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		

cameraCapture.release()
cv2.destroyAllWindows()
#wait for user press 0, if not, script will run and close the image 