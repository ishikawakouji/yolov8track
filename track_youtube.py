from ultralytics import YOLO

model = YOLO('yolov8n-pose.pt')
results = model.track(source="https://youtu.be/-0UAIEgmr_U", show=True)


