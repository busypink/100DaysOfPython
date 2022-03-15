alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#  ceaser cypher: se shift 3, a = d, b = e, c=f ...


def caesar(direction, text, shift):
    encoded = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift
        elif direction == "decode":
            new_position = position - shift
        new_letter = alphabet[new_position]
        encoded += new_letter
    print(f"Your {direction}d word is:\n {encoded}")


caesar(direction, text, shift)
