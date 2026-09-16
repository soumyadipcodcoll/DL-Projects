from pathlib import Path
from PIL import Image, ImageDraw


BASE = Path(__file__).parent

image_dir = BASE / "dataset" / "images"
label_dir = BASE / "dataset" / "labels"

# Take first 5 images
images = list(image_dir.glob("dog*.jpg"))[:2]

for image_path in images:

    label_path = label_dir / f"{image_path.stem}.txt"

    image = Image.open(image_path).convert("RGB")

    draw = ImageDraw.Draw(image)

    image_width, image_height = image.size

    # Read annotation
    with open(label_path, "r") as f:

        for line in f:

            parts = line.strip().split()

            if len(parts) != 5:
                continue

            class_id = int(parts[0])

            x_center = float(parts[1])
            y_center = float(parts[2])
            width = float(parts[3])
            height = float(parts[4])

            # Convert normalized coordinates
            x_center *= image_width
            y_center *= image_height

            width *= image_width
            height *= image_height

            # Convert center coordinates
            # to corner coordinates
            x1 = x_center - width / 2
            y1 = y_center - height / 2

            x2 = x_center + width / 2
            y2 = y_center + height / 2

            # Draw bounding box
            draw.rectangle(
                [x1, y1, x2, y2],
                outline="red",
                width=3
            )

            # Show class ID
            draw.text(
                (x1, y1),
                f"Class {class_id}",
                fill="red"
            )

    print(
        f"{image_path.name} | "
        f"Size: {image.size} | "
        f"Label: {label_path.name}"
    )

    image.show()