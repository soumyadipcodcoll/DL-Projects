from pathlib import Path
import random
import shutil


# --------------------------------
# Paths
# --------------------------------

BASE = Path(__file__).parent

source_images = BASE / "dataset" / "images"
source_labels = BASE / "dataset" / "labels"

output = BASE / "data"


# --------------------------------
# Split ratios
# --------------------------------

TRAIN_RATIO = 0.70
VAL_RATIO = 0.20
TEST_RATIO = 0.10


# --------------------------------
# Create directories
# --------------------------------

for split in ["train", "val", "test"]:

    (output / "images" / split).mkdir(
        parents=True,
        exist_ok=True
    )

    (output / "labels" / split).mkdir(
        parents=True,
        exist_ok=True
    )


# --------------------------------
# Find images
# --------------------------------

images = []

for extension in ["*.jpg", "*.jpeg", "*.png"]:

    images.extend(source_images.glob(extension))


print("Total images found:", len(images))


# --------------------------------
# Keep only images with labels
# --------------------------------

valid_images = []

missing_labels = []

for image in images:

    label = source_labels / f"{image.stem}.txt"

    if label.exists():
        valid_images.append(image)
    else:
        missing_labels.append(image.name)


print("Images with labels:", len(valid_images))
print("Images without labels:", len(missing_labels))


if missing_labels:

    print("\nMissing labels:")
    for name in missing_labels[:10]:
        print(name)


# --------------------------------
# Shuffle
# --------------------------------

random.seed(42)

random.shuffle(valid_images)


# --------------------------------
# Split
# --------------------------------

total = len(valid_images)

train_end = int(total * TRAIN_RATIO)

val_end = train_end + int(total * VAL_RATIO)


train_images = valid_images[:train_end]

val_images = valid_images[train_end:val_end]

test_images = valid_images[val_end:]


print("\nDataset split:")
print("Train:", len(train_images))
print("Val:", len(val_images))
print("Test:", len(test_images))


# --------------------------------
# Copy files
# --------------------------------

splits = {
    "train": train_images,
    "val": val_images,
    "test": test_images
}


for split, split_images in splits.items():

    for image in split_images:

        label = source_labels / f"{image.stem}.txt"

        # Copy image
        shutil.copy2(
            image,
            output / "images" / split / image.name
        )

        # Copy label
        shutil.copy2(
            label,
            output / "labels" / split / label.name
        )


print("\nDataset preparation completed!")