import pathlib
from PIL import Image
from torchvision.datasets import VisionDataset


class MNISTPrinted(VisionDataset):
    def __init__(self, root, transform=None):
        """
        Args:
            root (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on a sample.
            target_transform (callable, optional): Optional transform to be applied on the target.
        """
        super(MNISTPrinted, self).__init__(root, transform=transform)
        self.root = root
        self.transform = transform

        # Load all image file paths and labels
        self.image_paths = sorted(pathlib.Path(root).rglob('*.png'))
        self.labels = [int(image_path.stem[6]) for image_path in self.image_paths]
        

    def __len__(self):
        """Returns the total number of samples in the dataset."""
        return len(self.image_paths)


    def __getitem__(self, idx):
        """Generates one sample of data."""
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert('L')  # Convert image to grayscale
        
        label = self.labels[idx]
        
        if self.transform:
            image = self.transform(image)

        return image, label


# Example usage:
# from torchvision import transforms
# transform = transforms.Compose([
#     transforms.Resize((28, 28)),
#     transforms.ToTensor(),
# ])
# dataset = MNISTPrinted(root='path/to/mnist/printed', transform=transform)