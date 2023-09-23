from base64 import b64encode, b64decode

def hex_to_base64(input: str):
    str_b64 = b64encode(bytes.fromhex(input)).decode()
    print(str_b64)
    return str_b64

def hex_decoded(input: str):
    decoded = bytes.fromhex(input).decode('ascii')
    print(decoded)
    return decoded

def main():
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    hex_to_base64(input)
    # Hidden message:
    hex_decoded(input)

if __name__ == '__main__':
    main()


