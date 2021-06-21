import os
import shutil

root = '/media/SuperHisk/tiny-imagenet-200/'
source = os.path.join(root, 'val')
target = os.path.join(root, 'valfolder')

file = os.path.join(source, 'val_annotations.txt')
with open(file, 'r') as f:
    a = f.readlines()

for i in range(len(a)):
    name, cls = a[i].split()[:2]
    cls_path = os.path.join(target, cls)
    if not os.path.exists(cls_path):
        os.makedirs(cls_path)
    img_path = os.path.join(source, 'images', name)
    img_path_t = os.path.join(cls_path, name)
    shutil.copy(img_path, img_path_t)

print('done')
