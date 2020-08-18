import os

def prune(group):
    images = "images"
    annots = "annots"
    poplist = []
    for image in os.listdir(os.path.join(group,images)):
        name, ext = os.path.splitext(image)
        xml_pair = name + ".xml"
        if not os.path.exists(os.path.join(group,annots,xml_pair)):
            poplist.append(os.path.join(group,images,image))
    for annot in os.listdir(os.path.join(group,annots)):
        name, ext = os.path.splitext(annot)
        jpg_pair = name + ".jpg"
        if not os.path.exists(os.path.join(group,images,jpg_pair)):
            poplist.append(os.path.join(group,annots,annot))
    print("Missing pair in group", group)
    print(poplist)

print("Scanning data for images or annotations without corresponding values")
prune("validadate")
prune("train")