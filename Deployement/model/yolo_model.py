from ultralytics import YOLO

def load_model_yolo():
    return YOLO(r"model\bestV11.pt")
