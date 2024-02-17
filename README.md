# SteganoHide

SteganoHide is a Python script for steganographically hiding images inside the lower bits of other images. It uses the Pillow library for image processing.

## How It Works

Steganography is the practice of concealing messages or information within other non-secret data. In this script, we use steganography to hide one image (the hidden image) within another image (the cover image).

### Hiding an Image

When hiding an image within another image, we manipulate the RGB values of each pixel in both images. The least significant bits (LSBs) of the RGB values of the hidden image are embedded into the LSBs of the RGB values of the cover image. This process alters the cover image imperceptibly to the human eye.

### Extracting the Hidden Image

To extract the hidden image from the resulting image, we reverse the process. We retrieve the LSBs of the RGB values of each pixel from the output image. These LSBs contain the hidden image's data. By extracting and reconstructing these LSBs, we can recover the hidden image.

## Example :
### Cover Image :
![steg_nessi](https://github.com/GH0STH4CKER/SteganoHide/assets/62290930/96d3a282-2fbd-4163-9c1e-eaa20187168e)
### Hidden Image:
![download](https://github.com/GH0STH4CKER/SteganoHide/assets/62290930/aae98556-7571-4520-9b0c-b8ca2313ecaa)
