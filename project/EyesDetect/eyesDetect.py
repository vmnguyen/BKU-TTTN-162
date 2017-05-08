import cv2

#image path and cascade path
imagePath = "abba.png"
cascPath = "haarcascade_eye.xml"

#Create haar cascade classifier
eyesCascade = cv2.CascadeClassifier(cascPath)

#Detect from image
''' 



#Read image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Detect eyes
eyes = eyesCascade.detectMultiScale(
	gray,
	scaleFactor = 1.06,
	minNeighbors = 4,
	minSize = (5, 5),
	flags = cv2.CASCADE_SCALE_IMAGE
)

print "Found {0} eye(s) ".format(len(eyes))


for (x, y, w, h) in eyes:
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)
'''

# Detect from camera 

cameraCapture = cv2.VideoCapture(0)
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

	cv2.imshow('Video', frame)
	# Wait for key 'q' pressed to exit the loop
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cameraCapture.release()
cv2.destroyAllWindows()