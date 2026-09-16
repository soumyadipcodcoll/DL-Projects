from pathlib import Path

label_dir = Path("YOLO_cat_dog/dataset/labels")

label_files = list(label_dir.rglob("*.txt"))

print("Total label files:", len(label_files))

for file in label_files[:5]:
    print(file)

classes = set()
invalid = []

for file in label_files:

    with open(file, "r") as f:

        for line_number, line in enumerate(f, start=1):

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 5:
                invalid.append(
                    (file.name, line_number, line)
                )
                continue

            try:
                class_id = int(parts[0])

                x = float(parts[1])
                y = float(parts[2])
                w = float(parts[3])
                h = float(parts[4])

            except ValueError:
                invalid.append(
                    (file.name, line_number, line)
                )
                continue

            classes.add(class_id)

            # Check YOLO coordinates
            if not all(0 <= value <= 1 for value in [x, y, w, h]):
                invalid.append(
                    (file.name, line_number, line)
                )


print("Classes found:", sorted(classes))
print("Invalid annotations:", len(invalid))

print("\nFirst 5 annotation files:")

for file in label_files[:5]:

    print(f"\n{file.name}")

    with open(file, "r") as f:
        print(f.read().strip())