# from PIL import Image

# image = Image.open("images/spiderman.png")

# print("Image loaded successfully!")
# print("Image size:", image.size)
# print("Image mode:", image.mode)  


# # getting pixel
# pixel = image.getpixel((0, 0))
# print("First pixel:", pixel)  

# from PIL import Image

# image = Image.open("images/spiderman.png")

# pixel = image.getpixel((0, 0))

# print("Pixel:", pixel)

# red = pixel[0]
# green = pixel[1]
# blue = pixel[2]

# print("Red:", red)
# print("Green:", green)
# print("Blue:", blue)

# print("Red binary:", format(red, "08b"))
# print("Green binary:", format(green, "08b"))
# print("Blue binary:", format(blue, "08b"))


# new_red = red | 1

# print("New red:", new_red)
# print("New red binary:", format(new_red, "08b"))

# # Create a new RGB pixel
# new_pixel = (new_red, green, blue)

# # Change pixel at position (0, 0)
# image.putpixel((0, 0), new_pixel)

# # Save the modified image
# image.save("images/stego.png")

# print("Stego image saved!")

# check = image.getpixel((0, 0))
# print("Modified pixel:", check)


## secert message is "Hello"
# H → 01001000
# E → 01000101
# L → 01001100
# L → 01001100
# O → 01001111

# mesg: 01001000 01000101 01001100 01001100 01001111   

from PIL import Image

# Load the image
image = Image.open("images/spiderman.png")
image = image.convert("RGB")

# Secret message
message = "HELLO<END>"

# Convert message to binary
binary_message = ""

for character in message:
    binary_message += format(ord(character), "08b")

print("Message:", message)
print("Binary:", binary_message)
print("Number of bits:", len(binary_message))


def set_lsb(value, bit):
    if bit == "0":
        return value & 254
    else:
        return value | 1


# Hide the binary message inside pixel LSBs
bit_index = 0

width, height = image.size

for y in range(height):
    for x in range(width):

        pixel = image.getpixel((x, y))

        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        if bit_index < len(binary_message):
            red = set_lsb(red, binary_message[bit_index])
            bit_index += 1

        if bit_index < len(binary_message):
            green = set_lsb(green, binary_message[bit_index])
            bit_index += 1

        if bit_index < len(binary_message):
            blue = set_lsb(blue, binary_message[bit_index])
            bit_index += 1

        image.putpixel((x, y), (red, green, blue))

        if bit_index >= len(binary_message):
            break

    if bit_index >= len(binary_message):
        break


# Save the stego image
image.save("images/stego.png")

print("Message hidden successfully!")
print("Bits written:", bit_index)