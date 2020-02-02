def new_password_check(pwd):
    return len({char for char in pwd if char in 'abcdefghijklmnopqrstuvwxyz'}) > 0 and \
           len({char for char in pwd if char in '!@#$%ˆ&*()_+-='}) > 0

if __name__ == "__main__":
    p = input('Please enter your password: ')
    if new_password_check(p):
        print('Thank you')
    else:
        print('invalid password')