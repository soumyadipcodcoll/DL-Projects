from ultralytics import YOLO
from pathlib import Path

# Load trained model
model = YOLO(
    "D:/Git_project/Projects/DL/YOLO_cat_dog/Runs/cat_dog_train/weights/best.pt"
)

# Test images
image_dir = Path(
    "D:/Git_project/Projects/DL/YOLO_cat_dog/Data/images/test"
)

# Run prediction
results = model.predict(
    source=str(image_dir),
    imgsz=640,
    conf=0.25,
    save=True
)

# Print detections
for result in results:
    print("\nImage:", result.path)

    if len(result.boxes) == 0:
        print("No objects detected.")
        continue

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]

        print(f"  {class_name}: {confidence:.2f}")