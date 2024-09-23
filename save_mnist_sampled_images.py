import numpy as np
import cv2

# path = '/home/julian/work/minimal-diffusion/trained_models/UNet_mnist-250-sampling_steps-500_images-class_condn_True.npz'
# path = '/home/julian/work/minimal-diffusion/trained_models/0918/UNet_mnist-250-sampling_steps-500_images-class_condn_True.npz'
path = '/home/julian/work/minimal-diffusion/sampled_images/UNet_mnist-250-sampling_steps-500_images-class_condn_True.npz'
samples = np.load(path)

for idx, image in enumerate(samples['arr_0.npy']):
    grayImage = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(f'./sampled_images/sample_mnist_{idx}_{samples["arr_1.npy"][idx]}.png', grayImage)

