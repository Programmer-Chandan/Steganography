from PIL import Image

# Load the stego image
image = Image.open("images/stego.png").convert("RGB")

binary_message = ""

width, height = image.size

# Extract LSBs
for y in range(height):
    for x in range(width):

        red, green, blue = image.getpixel((x, y))

        binary_message += str(red & 1)
        binary_message += str(green & 1)
        binary_message += str(blue & 1)


# Convert binary to text
message = ""

for i in range(0, len(binary_message), 8):

    byte = binary_message[i:i + 8]

    if len(byte) < 8:
        break

    character = chr(int(byte, 2))
    message += character

    # Stop when END marker is found
    if message.endswith("<END>"):
        message = message[:-5]
        break


print("Decoded message:", message)