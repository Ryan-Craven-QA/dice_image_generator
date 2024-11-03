# Dice Image Generator 🎲

A powerful Python application that transforms images into artistic dice mosaics. This tool allows you to recreate any image using arrangements of dice faces, perfect for creating unique art installations, displays, or creative projects.

![submarineEx](https://github.com/user-attachments/assets/e8b45944-9483-4b18-83a3-99e2ac303174)

## 🌟 Features

- Convert any image into a dice-based representation
- Multiple dice options:
  - Monochrome (White or Black dice)
  - Combined (mix of White and Black dice)
  - Colored dice (White, Black, Red, Blue, Yellow)
- Support for different dice sizes:
  - Standard Dice (0.625")
  - Mini Dice (0.27")
  - Micro Dice (5mm/0.19685")
- Advanced dithering algorithm for optimal image reproduction
- Real-time preview of the generated dice pattern
- Export options:
  - Save layout as text file
  - Export to Excel spreadsheet
  - Save preview image
- Automatic calculation of required dice quantities
- User-friendly GUI interface

## 🚀 Getting Started

### Prerequisites

```bash
pip install pillow numpy tkinter openpyxl
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dice-image-generator.git
cd dice-image-generator
```

2. Ensure all dice images are in their respective folders:
```
dice_white/
dice_black/
dice_red/
dice_blue/
dice_yellow/
```

3. Run the application:
```bash
python dice_image_generator.py
```

## 📖 How to Use

1. **Enter Physical Dimensions**
   - Input the desired width and height in feet
   - The program will calculate the required number of dice

2. **Select Image**
   - Click "Browse" to choose your source image
   - Supported formats: JPG, JPEG, PNG, BMP, GIF

3. **Choose Dice Options**
   - Select dice type (Monochrome or Colored)
   - Choose specific dice options or colors
   - Select appropriate dice size

4. **Generate and Export**
   - Click "Generate Dice Image" to preview the result
   - Save the layout as text or Excel file
   - Export the preview image

## 🎨 Image Processing

The application uses the Floyd-Steinberg dithering algorithm to optimize the representation of images using dice faces. The process involves:

1. Converting the image to grayscale
2. Applying dithering for optimal tone distribution
3. Mapping grayscale values to appropriate dice faces
4. Generating a layout that matches the desired physical dimensions

## 📋 Output Formats

### Text Layout
```
    |  1  |  2  |  3  |  4  |
----+-----+-----+-----+-----+
  1 | Whi3| Whi4| Bla2| Bla1|
----+-----+-----+-----+-----+
```

### Excel Layout
- Organized grid showing dice positions
- Legend for dice face interpretations
- Color coding for easy reference

## 🔧 Customization

The code supports easy customization of:
- Dice colors and types
- Physical dimensions
- Dithering parameters
- Output formats
- Preview settings

## 📝 File Structure

```
├── dice_image_generator.py  # Main application
├── create_dice_face.py      # Dice face generator
├── dice_white/             # White dice images
├── dice_black/             # Black dice images
└── dice_[color]/           # Other colored dice images
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by various dice art installations
- Uses the PIL library for image processing
- Implements Floyd-Steinberg dithering algorithm

## ⚠️ Notes

- The aspect ratio of the input image should match the desired physical dimensions for best results
- Large installations may require significant quantities of dice
- Preview images are scaled for display purposes

## 🐛 Known Issues
