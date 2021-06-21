import os,sys
import numpy as np
import torch
from torchvision import datasets,transforms
from sklearn.utils import shuffle
from copy import deepcopy

def get(data_path,seed=0,pc_valid=0.10):
    data={}
    taskcla=[]
    size=[3,224,224]

    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    dat={}
    train_path = os.path.join(data_path, 'train')
    test_path = os.path.join(data_path, 'val')
    dat['train']=datasets.ImageFolder(train_path,transform=transforms.Compose([transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),transforms.Normalize(mean,std)]))
    dat['test']=datasets.ImageFolder(test_path,transform=transforms.Compose([transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean,std)
]))
    cla = 0
    for n in range(10):
        data[n]={}
        data[n]['name']='sub'+'-'+ str(cla)+ '-'+ str(cla+9)
        data[n]['ncla']=10
        data[n]['train']={'x': [],'y': []}
        data[n]['test']={'x': [],'y': []}
        cla += 10

    for s in ['train','test']:
        for nn in range(10):
            temp = deepcopy(dat[s])
            idx = []
            for c in range(10):
                cc = int(nn * 10 + c)
                tar = np.array(temp.targets)
                idx.extend(np.where(tar == cc)[0])
            imgs, tars = split_images_labels(temp.samples)
            _imgs = imgs[idx]
            _tars = tars[idx]
            _labels = _tars % 10
            _sample = merge_images_labels(_imgs, _labels)
            temp.imgs = temp.samples = _sample
            data[nn][s]['x'] = temp
    

    # Validation
    for t in data.keys():
        r=range(len(data[t]['train']['x']))
        r=np.array(shuffle(r,random_state=seed),dtype=int)
        nvalid=int(pc_valid*len(r))
        ivalid=r[:nvalid]
        itrain=r[nvalid:]
        data[t]['valid']={}
        data[t]['valid']['x']=torch.utils.data.Subset(data[t]['train']['x'], ivalid)
        data[t]['valid']['y']=[]
        data[t]['train']['x']=torch.utils.data.Subset(data[t]['train']['x'], itrain)
        data[t]['train']['y']=[]

    # Others
    n=0
    for t in data.keys():
        taskcla.append((t,data[t]['ncla']))
        n+=data[t]['ncla']
    data['ncla']=n

    return data,taskcla,size

def split_images_labels(imgs):
    images = []
    labels = []
    for item in imgs:
        images.append(item[0])
        labels.append(item[1])

    return np.array(images), np.array(labels)

def merge_images_labels(images, labels):
    images = images.tolist()
    labels = labels.tolist()
    assert(len(images)==len(labels))
    imgs = []
    for i in range(len(images)):
        item = (images[i], labels[i])
        imgs.append(item)
    
    return imgs

if __name__ == '__main__':
    get('/home/deepin/Documents/project/data/SubImageNet/')
