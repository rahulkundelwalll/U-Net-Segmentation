import os
from PIL import Image
from torch.utils.data.dataset import Dataset
from torchvision import transforms

class CarvanaDataset(Dataset):
    def __init__(self, root_path, test=False):
        self.root_path = root_path
        if test:
            self.images = sorted([os.path.join(root_path, "val", i) for i in os.listdir(os.path.join(root_path, "val")) if i.endswith(".jpg")])
            self.masks = sorted([os.path.join(root_path, "val_mask", i) for i in os.listdir(os.path.join(root_path, "val_mask")) if i.endswith(".png")])
        else:
            self.images = sorted([os.path.join(root_path, "train", i) for i in os.listdir(os.path.join(root_path, "train")) if i.endswith(".jpg")])
            self.masks = sorted([os.path.join(root_path, "train_mask", i) for i in os.listdir(os.path.join(root_path, "train_mask")) if i.endswith(".png")])
        
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()])

    def __getitem__(self, index):
        img = Image.open(self.images[index]).convert("RGB")
        mask = Image.open(self.masks[index]).convert("L")

        return self.transform(img), self.transform(mask)

    def __len__(self):
        return len(self.images)
