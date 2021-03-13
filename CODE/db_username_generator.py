import random

def create_username(*args):
    """ generating random username frpm the user given credentials"""
    user_name=''
    key_words=args[0].split(' ')
    first_part=random.choice(key_words)
    second_part=args[1][5:10]
    user_name=first_part+'@'+second_part
    return(user_name)