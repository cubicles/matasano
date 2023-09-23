from hex_to_b64 import hex_to_base64

def fixed_xor(input_1: str, input_2: str):
    ''' Takes 2 string inputs of same lenght and applies a XOR between each of
        their characters (binary). Final result is converted back to string

    '''
    print(len(input_1))
    print(len(input_2))

    if len(input_1) != len(input_2):
        print('LENGHT MISMATCH ERROR')
        return -1

    for idx, val in enumerate(input_1):
        print(input_1[idx], input_2[idx])


def house_binary():
    house_input = 'house'

    binary_representation = ' '

    for char in house_input:
        ascii_value = ord(char)
        binary_representation += format(ascii_value, '08b') + ' '

    print(binary_representation.strip())
    
def main():
    ''' Takes 2 string inputs. Decodes the first to base64
        and XORs them (Equal lenght buffers) to the input2
    '''
    # Inputs
    input_1 = '1c0111001f010100061a024b53535009181c'
    input_2 = '686974207468652062756c6c277320657965'
    # Decode
    print(bytes.fromhex(input_1).decode('ascii'))
    print(bytes.fromhex(input_2).decode('ascii'))


if __name__ == '__main__':
    main()

