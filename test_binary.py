# message = "HELLO"

# for character in message:
#     binary = format(ord(character), "08b")
#     print(character, "→", binary)

message = "HELLO"

binary_message = ""

for character in message:
    binary_message += format(ord(character), "08b")

print("Message:", message)
print("Binary:", binary_message)
print("Number of bits:", len(binary_message))