import torchvision
from torchvision import transforms
from .wrapper import CacheClassLabel
import os

def MNIST(dataroot, train_aug=False):
    # Add padding to make 32x32
    #normalize = transforms.Normalize(mean=(0.1307,), std=(0.3081,))  # for 28x28
    normalize = transforms.Normalize(mean=(0.1000,), std=(0.2752,))  # for 32x32

    val_transform = transforms.Compose([
        transforms.Pad(2, fill=0, padding_mode='constant'),
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.ToTensor(),
            normalize,
        ])

    # train_dataset = torchvision.datasets.MNIST(
    #     root=dataroot,
    #     train=True,
    #     download=True,
    #     transform=train_transform
    # )
    train_dataset = tmpMNIST(
        root=dataroot,
        train=True,
        download=True,
        transform=train_transform
    )
    train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.MNIST(
        dataroot,
        train=False,
        transform=val_transform
    )
    val_dataset = CacheClassLabel(val_dataset)

    return train_dataset, val_dataset

def CIFAR10(dataroot, train_aug=False):
    normalize = transforms.Normalize(mean=[0.491, 0.482, 0.447], std=[0.247, 0.243, 0.262])

    val_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])

    train_dataset = torchvision.datasets.CIFAR10(
        root=dataroot,
        train=True,
        download=True,
        transform=train_transform
        )
    # cifar102png(train_dataset, root=dataroot, train=True)
    train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.CIFAR10(
        root=dataroot,
        train=False,
        download=True,
        transform=val_transform
    )
    # cifar102png(val_dataset, root=dataroot, train=False)
    val_dataset = CacheClassLabel(val_dataset)

    return train_dataset, val_dataset


def CIFAR100(dataroot, train_aug=False):
    normalize = transforms.Normalize(mean=[0.507, 0.487, 0.441], std=[0.267, 0.256, 0.276])

    val_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])

    train_dataset = torchvision.datasets.CIFAR100(
        root=dataroot,
        train=True,
        download=True,
        transform=train_transform
    )
    train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.CIFAR100(
        root=dataroot,
        train=False,
        download=True,
        transform=val_transform
    )
    val_dataset = CacheClassLabel(val_dataset)

    return train_dataset, val_dataset

def TinyImageNet(dataroot, train_aug=False):
    traindir = os.path.join(dataroot, 'train')
    valdir = os.path.join(dataroot, 'val')
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    val_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(64, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])
    train_dataset = torchvision.datasets.ImageFolder(
        root=traindir,
        transform=train_transform
    )
    train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.ImageFolder(
        root=valdir,
        transform=val_transform
    )
    val_dataset = CacheClassLabel(val_dataset)
    return train_dataset, val_dataset

def FiveDatasets(dataroot, train_aug=False):
    traindir = os.path.join(dataroot, 'fivedataset/train')
    valdir = os.path.join(dataroot, 'fivedataset/val')
    normalize = transforms.Normalize(mean=[0.318, 0.318, 0.320], std=[0.272, 0.273, 0.275])

    val_transform = transforms.Compose([
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            normalize,
        ])
    train_dataset = torchvision.datasets.ImageFolder(
        root=traindir,
        transform=train_transform
    )
    train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.ImageFolder(
        root=valdir,
        transform=val_transform
    )
    val_dataset = CacheClassLabel(val_dataset)
    return train_dataset, val_dataset



from torchvision.datasets.mnist import read_image_file, read_label_file
from PIL import Image
class tmpMNIST(torchvision.datasets.MNIST):
    @property
    def raw_folder(self):
        return os.path.join(self.root, 'FashionMNIST', 'raw')
        # return os.path.join(self.root, 'MNIST', 'raw')

    def download(self):
        print('Processing...')
        training_set = (
            read_image_file(os.path.join(self.raw_folder, 'train-images-idx3-ubyte')),
            read_label_file(os.path.join(self.raw_folder, 'train-labels-idx1-ubyte'))
        )
        training_set_img = training_set[0].numpy()
        training_set_label = training_set[1].numpy()
        tr_folder = os.path.join(self.raw_folder, 'train')
        if not os.path.exists(tr_folder):
            os.mkdir(os.path.join(self.raw_folder, 'train'))
        for i, l in enumerate(training_set_label):
            path = os.path.join(tr_folder, str(l+30))
            if not os.path.exists(path):
                os.mkdir(path)
            img = Image.fromarray(training_set_img[i])
            img = img.resize((32,32))
            img = img.convert('RGB')
            file = os.path.join(path, str(i) + '.png')
            img.save(file)

        test_set = (
            read_image_file(os.path.join(self.raw_folder, 't10k-images-idx3-ubyte')),
            read_label_file(os.path.join(self.raw_folder, 't10k-labels-idx1-ubyte'))
        )
        test_set_img = test_set[0].numpy()
        test_set_label = test_set[1].numpy()
        tr_folder = os.path.join(self.raw_folder, 'val')
        if not os.path.exists(tr_folder):
            os.mkdir(os.path.join(self.raw_folder, 'val'))
        for i, l in enumerate(test_set_label):
            path = os.path.join(tr_folder, str(l+30))
            if not os.path.exists(path):
                os.mkdir(path)
            img = Image.fromarray(test_set_img[i])
            img = img.resize((32,32))
            img = img.convert('RGB')
            file = os.path.join(path, str(i) + '.png')
            img.save(file)

        print('Done!')

def SVNH(dataroot, train_aug=False):
    normalize = transforms.Normalize(mean=[0.4377, 0.4438, 0.4728], std=[0.198, 0.201, 0.197])

    val_transform = transforms.Compose([
        transforms.Pad(2, fill=0, padding_mode='constant'),
        transforms.ToTensor(),
        normalize,
    ])
    train_transform = val_transform
    if train_aug:
        train_transform = transforms.Compose([
            transforms.RandomCrop(32, padding=4),
            transforms.ToTensor(),
            normalize,
        ])

    train_dataset = torchvision.datasets.SVHN(
        root=dataroot,
        split='train',
        download=True,
        transform=train_transform
    )
    svnh2png(train_dataset, dataroot, 'train')
    # train_dataset = CacheClassLabel(train_dataset)

    val_dataset = torchvision.datasets.SVHN(
        dataroot,
        split='test',
        transform=val_transform
    )
    svnh2png(val_dataset, dataroot, 'val')
    # val_dataset = CacheClassLabel(val_dataset)

    return train_dataset, val_dataset
def svnh2png(dataset, root, split):
    print('Processing...')
    img = dataset.data.transpose(0,3,2,1)
    label = dataset.labels
    if split == 'train':
        folder = os.path.join(root, 'train')
    else:
        folder = os.path.join(root, 'val')
    if not os.path.exists(folder):
        os.mkdir(folder)
    for i, l in enumerate(label):
        path = os.path.join(folder, str(l + 20))
        if not os.path.exists(path):
            os.mkdir(path)
        image = Image.fromarray(img[i])
        file = os.path.join(path, str(i) + '.png')
        image.save(file)
    print('Done')

import pickle
import numpy as np
def notMNIST(dataroot, train_aug=False):
    folder = os.path.join(dataroot, 'notmnist')
    training_file = 'notmnist_train.pkl'
    testing_file = 'notmnist_test.pkl'
    with open(os.path.join(folder, training_file), 'rb') as f:
        train = pickle.load(f)
    train_data = train['features'].astype(np.uint8).squeeze(1)
    train_label = train['labels'].astype(np.uint8)
    print('Processing training...')
    tr_folder = os.path.join(folder, 'train')
    if not os.path.exists(tr_folder):
        os.mkdir(tr_folder)
    for i, l in enumerate(train_label):
        path = os.path.join(tr_folder, str(l + 40))
        if not os.path.exists(path):
            os.mkdir(path)
        img = Image.fromarray(train_data[i])
        img = img.convert('RGB')
        file = os.path.join(path, str(i) + '.png')
        img.save(file)
    print('Done')
    with open(os.path.join(folder, testing_file), 'rb') as f:
        test = pickle.load(f)
    test_data = test['features'].astype(np.uint8).squeeze(1)
    test_label = test['labels'].astype(np.uint8)
    print('Processing testing...')
    te_folder = os.path.join(folder, 'val')
    if not os.path.exists(te_folder):
        os.mkdir(te_folder)
    for i, l in enumerate(test_label):
        path = os.path.join(te_folder, str(l + 40))
        if not os.path.exists(path):
            os.mkdir(path)
        img = Image.fromarray(test_data[i])
        img = img.convert('RGB')
        file = os.path.join(path, str(i) + '.png')
        img.save(file)
    print('Done')


def cifar102png(dataset, root, train):
    print('Processing...')
    img = dataset.data
    label = np.array(dataset.targets)
    if train:
        folder = os.path.join(root, 'train')
    else:
        folder = os.path.join(root, 'val')
    if not os.path.exists(folder):
        os.mkdir(folder)
    for i, l in enumerate(label):
        path = os.path.join(folder, str(l))
        if not os.path.exists(path):
            os.mkdir(path)
        image = Image.fromarray(img[i])
        file = os.path.join(path, str(i) + '.png')
        image.save(file)
    print('Done')
