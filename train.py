from ultralytics import YOLO


model = YOLO('yolov8n.pt')


result = model.train(
    data='HomeObjects-3k.yaml',
    epochs = 100,
    imgsz = 640,
    name = 'yolov8n_household_objects_detection'
)
