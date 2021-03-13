from werkzeug.security import generate_password_hash,check_password_hash
from db_connect import connect
import psycopg2
from db_farmer_search import farmer_info


def login_verify(args):
    
    connection=connect()
    username=args['username']
    password=args['password']
    
    command="""select * from user_login_details where username=%s;"""

    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchone()
        connection.commit()
        if check_password_hash(result[1],password):
            data=farmer_info(username)
            return(data)
        else:
            return(False)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("success")
