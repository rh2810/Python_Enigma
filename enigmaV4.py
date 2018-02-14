import string
"""
Class encrypts and decrypts messages, similar to an Enigma Machine.
"""


class Enigma:
    # Table that wil hold ciphered keys and values
    global table
    table = {}
    # List of valid character input
    global reference_table
    reference_table = list(string.printable)

    def main():
        encrypt = ""  # String used for encryption
        decrypt = ""  # String used for decryption
        i = j = 0     # increment variables
        k = 0

        # reference_table is mapped to integer values
        for j in reference_table:
            # map a casted integer to a table value
            table[j] = str(k).zfill(2)
            k += 1
        while True:
            # obtain input from user
            options = input("Enter 'e' to encrypt, 'd' to decrypt, 't' to" +
                            " display table, or 'q' to quit: ")

            # if the user enters an 'e', encrypt the message
            if options == 'e' or options == 'E':
                user_input = input("    What's the message?: ")
                for c in user_input:
                    for key in table:
                        if c == key:
                            # add each matching character one at a time to
                            # the encrypted message
                            encrypt += table.get(key)
                print("     Original message: " + user_input)
                print("     Encrypted message: " + encrypt)

            # if the user enters an 'd', decrypt the message
            elif options == 'd' or options == 'D':
                user_input = input("    What's the message?: ")
                while i < len(user_input):
                    for key in table:
                        if user_input[i:i+2] == table.get(key):
                            # add each matching character one at a time to
                            # the decrypted message
                            decrypt += key
                    i += 2
                print("     Original message: " + user_input)
                print("     Decrypted message: " + decrypt)

            # displays a table for cipher reference
            elif options == 't' or options == 'T':
                i = 0
                print('{', end='')
                for key in table:
                    if ((i % 6) == 0) & (i != 0):
                        print("")
                    if i == 96:
                        print("\'\\n\' = 96")
                    else:
                        print(key + " = " + table.get(key) + '; ', end='')
                    i = i+1

                print('}')

            # if the user enters an 'q', exit the while loop
            elif options == 'q' or options == 'Q':
                break

            i = 0
            encrypt = ""
            decrypt = ""

    if __name__ == "__main__":
        main()