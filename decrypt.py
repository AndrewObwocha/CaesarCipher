
'''
Caesar Cipher Decrypter
---------------------------------------------------
This script allows the user to decrypt a stored
website-password pair according to Caesar cipher
encryption

Author: Andrew Obwocha
Date: 19th Jan
'''

def file_reader(filename: str) -> list:
    '''
    Reads the contents of a file 

    Args:
        filename (str): Name of the file
    
    Returns:
        list: Lines of the file stored as a list
    '''
    with open(filename, 'r') as file:
        file_content = file.read()
    file_lines = file_content.splitlines()
    return file_lines


def decrypter(encrypted_data: str, shift_key: int) -> str:
    '''
    Decrpyts data according to shift_key and encryption source

    Args:
        encrypted_data (str): Data to be decrypted
        shift_key (int): Positions to shift key by
    
    Returns:
        str: Decrypted version of the data
    '''
    
    encryption_source = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "
    decrypted_data = ''
    for character in encrypted_data:
        index = encryption_source.find(character) + shift_key
        if index >= len(encryption_source):
            index -= len(encryption_source)
        decrypted_data += encryption_source[index]
    return decrypted_data        



def file_decrypter(filename: str) -> str:
    '''
    Reads through the file and decrypts the file data based on
    recorded shift key and the encryption source

    Args:
        filename (str): Name of the file
    
    Returns:
        dictionary: Webstie-Password pairs
    '''

    web_pass_pairs = {}
    file_lines = file_reader(filename)
    shift_key = int(file_lines[0])
    for index in range(1, len(file_lines), 2):
        website = decrypter(file_lines[index], shift_key)
        password = decrypter(file_lines[index+1], shift_key)
        web_pass_pairs[website] = password
    
    return web_pass_pairs


def main():
    file = input('Enter filename: ')
    web_pass_pairs = file_decrypter(file)

    repeat = True
    while repeat:
        user_website = input('\nEnter a website: ').lower().strip()
        
        password = web_pass_pairs.get(user_website, None)
        if password:
            print(f'Password for {user_website} is \'{password}\'')
        else:
            print('The website doesn\'t exist')
        
        choice = input('\nGet another password? (y/n): ')
        if choice == 'n':
            print('Goodbye!')
            repeat = False


if __name__ == '__main__':
    main()