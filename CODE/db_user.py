from db_tables import table
from db_connect import connect
from db_username_generator import create_username
from werkzeug.security import generate_password_hash,check_password_hash
from db_insert import insert_details,delete_details
from panda_data import data
import json
from db_get import get_user_login_details


def user_details(data):
    """ user details process in db"""
    conn=connect()
    user_name=create_username(data['Name'],data['PhNo'])
    pass_word=generate_password_hash(data['PhNo'])
    # c=check_password_hash(password,data['PhNo'])

    values=list(data.values())

    for n,i in enumerate(values):
        if i=="":
            values[n]=None
    print(values)
    # print(len(values))

    # # process1
    user=table(conn,user_name,pass_word)
    user.user_login_details()
    user.user_personal_details(values[0:6])
    user.user_agro_details(values[6:12])
    user.user_crop_details(values[12:21])  


    # login_details=get_user_login_details(conn,user_name) 
    
    # print(user.get_user_crop_details())
    

    # procss2
    # user=table(conn,user_name,pass_word,values)
    # user.insert_details()
    # user.delete_details()

    # process3
    # insert_details(conn,user_name,pass_word,values)
    # delete_details(conn)
    return(user_name)

if __name__=="__main__":
    pass