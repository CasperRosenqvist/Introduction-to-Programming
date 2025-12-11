
def text_input():
    text = input("Enter text to encrypt: ")
    return text

def show_positions(positions):
    print(f"Rotor positions: {positions[0]}, {positions[1]}, {positions[2]}")

def pass_forward(letter, rotor, position):
    index = (ord(letter) - ord('A') + position) % 26
    return rotor[index]

def pass_backward(letter, rotor, position):
    index = rotor.index(letter)
    return chr((index - position) % 26 + ord('A'))

def process_char(char, rotors, positions, reflector):
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26
    for i in range(3):
        char = pass_forward(char, rotors[i], positions[i])
    return char

def encrypt_text(text, rotors, positions, reflector):
    result = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            result += process_char(char, rotors, positions, reflector)
            show_positions(positions)
        else:
            result += char
    return result

def main():
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    rotors = [rotor1, rotor2, rotor3]
    positions = [0, 0, 0]
    print("Program starting.")
    print("Welcome to the Enigma machine!")
    text = text_input()
    encrypted = encrypt_text(text, rotors, positions, reflector)
    print("Encrypted text:", encrypted)
    print("Program ending.")

if __name__ == "__main__":
    main()
