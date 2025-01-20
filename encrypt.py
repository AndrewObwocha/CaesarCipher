
'''
Caesar Cipher Encrypter
---------------------------------------------------
This script allows the user to encrypt and store
website-password pairs according to Caesar cipher
technique

Author: Andrew Obwocha
Date: 19th Jan
'''


def validate_password(password: str) -> str:
    '''
    Evaluates whether a password is valid

    Args:
        password (str): Password to be validated
    
    Returns:
        str: The valid password if all conditions are met
        None: If the password fails validation, issues are printed
    '''

    issues = []
    if len(password) < 8:
        issues.append('\tPassword should be at least 8 characters')
    if ' ' in password:
        issues.append('\tPassword cannot have spaces')
    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_numeric = any(char.isdigit() for char in password)
    has_special = any(char in '!@#$%^&*?' for char in password)
    invalid_chars = list(dict.fromkeys(char for char in password if not (char.isalnum() or char in '!@#$%^&*?' or char == ' ')))
    
    if not has_uppercase:
        issues.append('\tMissing an uppercase letter in the password')
    if not has_lowercase:
        issues.append('\tMissing a lowercase letter in the password')
    if not has_special:
        issues.append('\tMissing a special character in the password')
    if not has_numeric:
        issues.append('\tMissing a digit in the password')
    if invalid_chars:
        invalid_characters = ', '.join(invalid_chars)
        issues.append(f'\t{invalid_characters} are not allowed in the password')

    if issues:
        print('\nIssues:')
        for issue in issues:
            print(issue)
        return None
    else:             
        return password            


def encrypter(data: str, shift_key: int) -> str:
    '''
    Encrpyts data according to shift_key and encryotion source
    
    Args:
        data (str): Data to be encrypted
        shift_key (int): Positions to shift key by

    Returns:
        str: Encrypted version of the data
    '''
    encryption_source = r"7elL2GJVkrv0dQ%Eb?N6uw*#t!@hYAop&O^a3FWCyKUT4PR5zBjDH8XgZnf9qMm1cSIsi$x "
    encrypted_data = ''
    for character in data:
        encrypted_data += encryption_source[encryption_source.find(character) - shift_key]
    
    return encrypted_data


def main():
    shift_key = int(input('Enter the Encryption key: '))
    with open('saved_passwords.txt', 'w') as file:
        file.write(str(shift_key))
    
    repeat = True
    while repeat:
        website = input('\nEnter website: ')
        parsed_website = website.lower().strip()

        password = input('Enter password: ')
        valid_password = validate_password(password)
        while not valid_password:
            print('\nPlease enter a strong valid password')
            password = input('Enter password: ')
            valid_password = validate_password(password)

        encrypted_website = encrypter(parsed_website, shift_key)
        encrypted_password = encrypter(valid_password, shift_key)
        
        with open('saved_passwords.txt', 'a') as file:
            file.write(f'\n{encrypted_website}')
            file.write(f'\n{encrypted_password}')

        print(f'\nPassword for {parsed_website} has been encrypted and stored successfully')
        choice = input('Add another password? (y/n): ')
        if choice == 'n':
            print('Goodbye!')
            repeat = False


if __name__ == '__main__':
    main()
