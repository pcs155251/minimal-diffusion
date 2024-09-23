from PIL import Image, ImageDraw, ImageFont
import os
import pathlib
import itertools

# Specify the directory where your fonts are located
# font_dir = "path_to_your_fonts_directory"  # Change this to your font directory
font_dir = '/usr/share/fonts/truetype/'
output_dir = "./digits_images/"  # Output directory for images
pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)

# List of digits to create images for
digits = [str(i) for i in range(10)]

# Get all font files from the specified directory
font_files = sorted(pathlib.Path(font_dir).rglob('*.ttf'))
print(len(font_files))

img_size = 28
font_sizes = list(range(25, 29)) # 4
angles = list(range(-15, 16, 5))
shift_xs = list(range(4))
shift_ys = list(range(4))
print(f'number of combinations: {len(font_sizes) * len(angles) * len(shift_xs) * len(shift_ys)}')

# Generate images for each digit and each font
for font_path in font_files[:1]:
    for digit, font_size, angle, shift_x, shift_y in itertools.product(digits, font_sizes, angles, shift_xs, shift_ys):
        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Create a new image with white background
        img = Image.new('RGB', (img_size, img_size), color='black')
        draw = ImageDraw.Draw(img)

        # Get bounding box for text to calculate its size
        bbox = draw.textbbox((0, 0), digit, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate text position to center it
        position_x = (img_size - text_width) // 2 + shift_x  # Center horizontally
        position_y = (img_size - text_height) // 2 + shift_y# Center vertically

        draw.text((position_x, position_y), digit, fill='white', font=font, anchor='lt')
        img = img.rotate(angle, expand=True)  # Change the angle as needed

        # Save the image with a unique name based on digit and font name
        font_name = os.path.basename(font_path).split('.')[0]  # Get font name without extension
        img.save(os.path.join(output_dir, f"{font_name}_{digit}_sz{font_size}_ang{angle}_x{shift_x}_y{shift_y}.png"))

print("Images created successfully!")