
from ultralytics import YOLO

model = YOLO(model = 'best.pt')

validation = model.val()

print('mAP :-' , validation.results_dict)
