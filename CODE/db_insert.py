import psycopg2
from db_connect import connect

def delete_details(connection):
    """ table for retrieving user crop details """
    command="""
    delete from user_login_details;       
    """
    command1="""
    delete from user_agro_details;       
    """
    command2="""
    delete from user_personal_details;       
    """
    command3="""
    delete from user_crop_details;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command1)
        cur.execute(command2)
        cur.execute(command3)
        cur.execute(command)
        connection.commit()
        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            return("success")


def insert_details(conn,username,password,args):
    """ table for storing the user credentialls """

    connection=conn
    user_name=username
    pass_word=password

    command1="""
    insert into user_login_details(username,password) values(%s,%s);
    """
    command2=""" 
    insert into user_personal_details(fullname,age,phonenumber,adress,state,district,mandal,username) values(%s,%s,%s,%s,%s,%s,%s,%s);
    """
    command3="""insert into user_agro_details(username,placeofland,landtype,landarea,culture,kind,crop) values(%s,%s,%s,%s,%s,%s,%s);"""
    command4="""insert into user_crop_details(username,year1,crop1,production1,year2,crop2,production2,year3,crop3,production3) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

    try:
        cur=connection.cursor()
        cur.execute(command1,(user_name,pass_word))
        cur.execute(command2,(args[0],args[1],args[2],args[3],'ANDHRA PRADESH',args[4],args[5],user_name))
        cur.execute(command3,(user_name,args[6],args[7],args[8],args[9],args[10],args[11]))
        cur.execute(command4,(user_name,args[12],args[13],args[14],args[15],args[16],args[17],args[18],args[19],args[20]))
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        return(error)
    finally:
        if connection is not None:
            connection.close()
            return("success")



def crop_cost():
    import json
    conn=connect()
    with open("datasets/crop_invest_per_acre.json") as f:
        c=json.load(f)
        # print(len(c))
    command="""update crops set cost=%s where lower(crop)=lower(%s);"""
    for i in c.keys():
        val=c[i]
        print(val,i)
        cur=conn.cursor()
        cur.execute(command,(val,i))
        conn.commit()

 

if __name__=="__main__":
    pass
