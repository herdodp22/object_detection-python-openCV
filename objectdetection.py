import cv2 


car_cascade = cv2.CascadeClassifier('C:/users/user/appdata/local/programs/python/python39/cars.xml')
body_cascade = cv2.CascadeClassifier('C:/users/user/appdata/local/programs/python/python39/haarcascade_fullbody.xml')

cap= cv2.VideoCapture('C:/users/user/appdata/local/programs/python/python39/peoplecut1.mp4')
 
while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    car = car_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in car:
       recta1 = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
       cv2.putText(recta1, 'car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    body = body_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in body :
        recta2 = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2 )
        cv2.putText(recta2, 'people', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 215, 0), 2 )
    
    frames = cv2.resize(frame, (800,600))
    cv2.imshow('herdo cam', frames)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break