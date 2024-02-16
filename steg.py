from PIL import Image

# Function to hide an image within another image
def hide_image(hidden_path, cover_path, output_path):
    # Open the images
    hidden_img = Image.open(hidden_path)
    cover_img = Image.open(cover_path)

    # Ensure both images have the same size
    if hidden_img.size != cover_img.size:
        raise ValueError("Images must have the same dimensions")

    # Get the pixel access objects for both images
    hidden_pixels = hidden_img.load()
    cover_pixels = cover_img.load()

    # Create a new image to store the result
    result_img = Image.new("RGB", hidden_img.size)
    result_pixels = result_img.load()

    # Loop through each pixel
    for x in range(hidden_img.width):
        for y in range(hidden_img.height):
            # Get the RGB values of the pixels
            hidden_r, hidden_g, hidden_b = hidden_pixels[x, y]
            cover_r, cover_g, cover_b = cover_pixels[x, y]

            # Hide the hidden image in the lower bits of the cover image
            result_pixels[x, y] = (
                (cover_r & 0b11111100) | (hidden_r >> 6),
                (cover_g & 0b11111100) | (hidden_g >> 6),
                (cover_b & 0b11111100) | (hidden_b >> 6)
            )

    # Save the result image
    result_img.save(output_path)
    print("Image hidden successfully!")


# Function to unhide an image from another image
def unhide_image(hidden_path, output_path):
    # Open the hidden image
    hidden_img = Image.open(hidden_path)

    # Create a new image to store the extracted hidden image
    extracted_img = Image.new("RGB", hidden_img.size)
    extracted_pixels = extracted_img.load()

    # Loop through each pixel
    for x in range(hidden_img.width):
        for y in range(hidden_img.height):
            # Get the RGB values of the pixel
            r, g, b = hidden_img.getpixel((x, y))

            # Extract the hidden bits
            extracted_pixels[x, y] = (
                (r & 0b00000011) << 6,
                (g & 0b00000011) << 6,
                (b & 0b00000011) << 6
            )

    # Save the extracted image
    extracted_img.save(output_path)
    print("Image extracted successfully!")


# Example usage
# Hide an image inside another image
    
# hide_image("hidden_image.png", "cover_image.png", "output_image.png")

# Extract the hidden image from the resulting image
    
#unhide_image("output_image.png", "extracted_image.png")
