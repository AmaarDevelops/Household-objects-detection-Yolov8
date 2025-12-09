from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

confidence_threshold = 0.30

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Error while opening the camera')
    exit()

print("Webcam feed opened, please press 'q' to open them")

while True:
    ret,frame = cap.read()

    if not ret:
        break


    results = model.predict(
        source = frame,
        conf = confidence_threshold,
        imgsz = 650,
        stream = False,
        verbose= False
    )

    annonated_frame = results[0].plot()

    cv2.imshow("Household item detection - press 'q' to exit",annonated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
