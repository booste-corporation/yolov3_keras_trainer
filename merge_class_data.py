import os

os.makedirs("train/images", exist_ok=True)
os.makedirs("train/annots", exist_ok=True)
os.makedirs("validate/images", exist_ok=True)
os.makedirs("validate/annots", exist_ok=True)

print("Consolidating images into train folder")
orig_path = os.path.abspath("openimages/")
contents = os.listdir(orig_path)
for path in contents:
    class_path = os.path.join(orig_path, path)
    if os.path.isdir(class_path):
        print("Moving", path)
        images_path = os.path.join(class_path, "images")
        annot_path = os.path.join(class_path, "pascal")
        for f in os.listdir(images_path):
            filepath = os.path.join(images_path,f)
            os.rename(filepath, os.path.join("train/images", f))
        for f in os.listdir(annot_path):
            filepath = os.path.join(annot_path,f)
            os.rename(filepath, os.path.join("train/annots", f)) 
print("Success")