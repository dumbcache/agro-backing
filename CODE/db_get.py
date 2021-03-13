import psycopg2

def get_details_by_location(connection,*arg):
    """ table for storing user agro details """
    command="""
    select username from user_personal_details where district=%s and mandal=%s;       
    """
    try:
        cur=connection.cursor()
        print(arg,"location")
        cur.execute(command,(arg[0],arg[1],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_details_by_crop(connection,arg):
    """ table for storing user agro details """
    command="""
    select username from user_agro_details where crop in %s;       
    """
    try:
        cur=connection.cursor()
        print(arg,"crop")
        cur.execute(command,(arg,))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_details_by_cost(connection,*arg):
    """ table for storing user agro details """
    command="""
    select username from user_agro_details inner join crops on user_agro_details.crop=crops.crop where cost between %s and %s;       
    """
    try:
        cur=connection.cursor()
        print(arg,"cost")
        cur.execute(command,(arg[0],arg[1],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)
    
def get_details_by_rl(connection,*arg):
    """ table for storing user agro details """
    command="""
    select P.username from user_personal_details P inner join user_agro_details A on P.username=A.username and P.district=%s and P.mandal=%s inner join crops C on C.crop=A.crop and C.cost between %s and %s;      
    """
    try:
        cur=connection.cursor()
        print(arg,"rl")
        cur.execute(command,(arg[2],arg[3],arg[0],arg[1],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_details_by_rlc(connection,*arg):
    """ table for storing user agro details """
    command="""
     select A.username from user_agro_details A inner join user_personal_details P on A.username=P.username and p.district=%s and p.mandal=%s inner join crops C on A.crop=C.crop where cost between %s and %s and A.crop in %s;      
    """
    try:
        cur=connection.cursor()
        print(arg,"rlc")
        cur.execute(command,(arg[2],arg[3],arg[0],arg[1],arg[4],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_details_by_rc(connection,*arg):
    """ table for storing user agro details """
    command="""
     select username from user_agro_details A inner join crops C on A.crop=C.crop where cost between %s and %s and A.crop in %s;      
    """
    try:
        cur=connection.cursor()
        print(arg,"rc")
        cur.execute(command,(arg[0],arg[1],arg[2],))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_details_by_lc(connection,district,mandal,arg):
    """ table for storing user agro details """
    command="""
     select P.username from user_personal_details P inner join user_agro_details A on P.username=A.username  where P.district=%s and P.mandal=%s and A.crop in %s;      
    """
    try:
        cur=connection.cursor()
        print(arg,"lc")
        cur.execute(command,(district,mandal,arg,))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def farmer_details(connection,arg):
    """ table for storing user agro details """
    command="""
    select * from user_personal_details p inner join user_agro_details a on p.username=a.username inner join user_crop_details c on a.username=c.username and p.username=%s;      
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(arg,))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)

def get_user_login_details(connection,username):
    """ table for storing user login details """
    command="""
    select * from user_login_details where username=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)


def get_user_personal_details(connection,username):
    """ table for retrieving user personal details """
    command="""
    select * from user_personal_details where username=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)


def get_user_agro_details(connection,username):
    """ table for retrieving user agro details """
    command="""
    select * from user_agro_details where username=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            return(result)


def get_user_crop_details(connection,username):
    """ table for retrieving user crop details """
    command="""
    select * from user_crop_details where username=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)


def after_register(connection,username):
    """ table for retrieving user personal details """
    command="""
    select username,phonenumber from user_personal_details where username=%s;       
    """
    try:
        cur=connection.cursor()
        cur.execute(command,(username,))
        result=cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            return(result)
