from ultralytics import YOLO

# Load pretrained YOLO11 nano model
model = YOLO("YOLO_cat_dog/models/yolo11n.pt")

# Fine-tune on Cat vs Dog dataset
results = model.train(
    data="YOLO_cat_dog/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    device="cpu",
    workers=2,
    project="YOLO_cat_dog/runs",
    name="cat_dog_train"
)

print("Training completed!")