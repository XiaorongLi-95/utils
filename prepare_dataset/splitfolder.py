import pickle
import numpy as np
from torchvision.datasets import CIFAR100
from PIL import Image
from torchvision import transforms
import os

normalize = transforms.Normalize(mean=(0.1000,), std=(0.2752,))
LABELS = list(range(100))
val_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])
train_dataset = CIFAR100(
        root='./dat',
        train=True,
        download=True,
        transform=val_transform
    )
val_dataset = CIFAR100(
        root='./dat',
        train=False,
        download=True,
        transform=val_transform
    )
for split in [10, 20]:
    cls_per_task = int(100 / split)
    path_ = '{}split'.format(split)
    for mode in ['train', 'test']:
        if mode == 'train':
            dataset = train_dataset
        else:
            dataset = val_dataset
        name = 1
        for (data, label) in zip (dataset.data, dataset.targets):
            for task in range(split):
                dirpath = os.path.join(path_, mode, str(task))               
                if label in LABELS[task*cls_per_task:(task+1)*cls_per_task]:
                    path = os.path.join(dirpath, str(label))
                    if not os.path.exists(path):
                        os.system("mkdir -p {}".format(path))
                    image = Image.fromarray(data)
                    image = image.convert('RGB')
                    filepath = os.path.join(path, str(name)+'.png')
                    image.save(filepath)
                    name += 1
                else:
                    continue

                
            
           

                
        
