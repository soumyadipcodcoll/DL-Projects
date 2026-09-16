---
license: apache-2.0
task_categories:
- object-detection
tags:
- yolo
- vision
- biology
pretty_name: Cat and Dog YOLO Dataset
size_categories:
- n<1K
---

# Cat and Dog Detection Dataset (YOLO Format)
This dataset is designed for training and evaluating object detection models, specifically **YOLOv8**, **YOLOv10**, or **YOLO11**, to identify cats and dogs in images.

## Dataset Structure
The dataset follows the standard YOLO object detection format:

- **images/**: Contains the raw images (`.jpg`, `.png`).
- **labels/**: Contains the corresponding bounding box annotations in `.txt` files.

### Annotation Format
Each label file contains annotations in the following format:
`<class_id> <x_center> <y_center> <width> <height>`

**Classes:**
- `0`: Cat
- `1`: Dog

## How to Use with Ultralytics
To use this dataset with the `ultralytics` library, create a `data.yaml` file pointing to this directory:

```yaml
path: ./dataset
train: images
val: images

names:
  0: dog
  1: cat
```

## Dataset Summary
- Total Images: 938
- Categories: Cat, Dog
- Format: YOLOv8 Text Format
- Purpose: Educational / Small-scale testing

## Maintenance
Developed and maintained by L.C. Sankalpa Lokuliyanage.

