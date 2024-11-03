from PIL import Image, ImageDraw, ImageOps
import os


# Function to create a dice face
def create_dice_face(number, dice_color, dot_color, size=200):
    # Create a square image with the dice color
    img = Image.new('RGB', (size, size), color=dice_color)
    draw = ImageDraw.Draw(img)

    # Dot positions (normalized coordinates)
    positions = {
        1: [(0.5, 0.5)],
        2: [(0.25, 0.25), (0.75, 0.75)],
        3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
        4: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.75), (0.75, 0.75)],
        5: [(0.25, 0.25), (0.75, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.75)],
        6: [(0.25, 0.25), (0.75, 0.25), (0.25, 0.5), (0.75, 0.5), (0.25, 0.75), (0.75, 0.75)]
    }

    # Draw the dots
    dot_radius = size * 0.08  # Adjust dot size as needed
    for pos in positions[number]:
        x = pos[0] * size
        y = pos[1] * size
        leftUpPoint = (x - dot_radius, y - dot_radius)
        rightDownPoint = (x + dot_radius, y + dot_radius)
        draw.ellipse([leftUpPoint, rightDownPoint], fill=dot_color)

    return img


# List of dice colors to generate
dice_colors = {
    'white': ('white', 'black'),
    'black': ('black', 'white'),
    'red': ('red', 'white'),
    'blue': ('blue', 'white'),
    'yellow': ('yellow', 'white')
}

# Generate dice faces for each color
for color_name, (dice_color, dot_color) in dice_colors.items():
    folder_name = f'dice_{color_name}'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    for i in range(1, 7):
        img = create_dice_face(i, dice_color=dice_color, dot_color=dot_color)
        img.save(f'{folder_name}/{i}.png')
    # Create solid dice images
    solid_dice = Image.new('RGB', (200, 200), color=dice_color)
    solid_dice.save(f'{folder_name}/solid_{color_name}.png')

print("Dice face images have been generated for all colors.")
