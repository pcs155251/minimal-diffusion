from torchvision import transforms
from easydict import EasyDict
from data import get_dataset, get_metadata
import os 

metadata = EasyDict(
    {
        "image_size": 28,
    }
)
mnist_metadata = get_metadata("mnist")

mnist_dataset = get_dataset("mnist", "./dataset", mnist_metadata)
mnistp_dataset = get_dataset("mnist_printed", "./dataset/MNIST_printed", metadata)

idx = 0

image, label = mnist_dataset[idx]  # Get image and label
# Convert tensor to PIL Image for saving
image = transforms.ToPILImage()(image)
# Define the filename using the index and label
filename = os.path.join('./', f"mnist_{label}_{idx}.png")
# Save the image
image.save(filename)


image, label = mnistp_dataset[idx]  # Get image and label
# Convert tensor to PIL Image for saving
image = transforms.ToPILImage()(image)
# Define the filename using the index and label
filename = os.path.join('./', f"mnistp_{label}_{idx}.png")
# Save the image
image.save(filename)