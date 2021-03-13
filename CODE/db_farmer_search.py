from db_connect import connect
from db_get import farmer_details,get_user_crop_details,get_user_login_details,get_user_agro_details,get_user_personal_details,get_details_by_location,get_details_by_crop,get_details_by_cost,get_details_by_rl,get_details_by_rc,get_details_by_rlc,get_details_by_lc
import json

conn=connect()

def send_details(args):
    start=args['start']
    end=args['end']
    district=args['district']
    mandal=args['mandal']
    crops=tuple(json.loads(args['crops']))
    # print(type(crops))
    if start==''or start=='0':
        start=None
    if end=='' or end=='0':
        end=None
    if district=='':
        district=None
    if len(crops)==0:
        crops=None
    result=farmer_search(start,end,district,mandal,crops)
    # print(start,end,district,mandal,crops)
    # print(result)
    return(result)


def farmer_search(range1=None,range2=None,district=None,mandal=None,crops=None):
    if range1 and range2 and district and mandal and crops:
        return(get_details_by_rlc(conn,range1,range2,district,mandal,crops))

    elif range1 and range2 and district and mandal:
        return(get_details_by_rl(conn,range1,range2,district,mandal))

    elif range1 and range2 and crops:
        return(get_details_by_rc(conn,range1,range2,crops))

    elif district and mandal and crops:
        return(get_details_by_lc(conn,district,mandal,crops))

    elif range1 and range2:
        return(get_details_by_cost(conn,range1,range2))

    elif district and mandal:
        return(get_details_by_location(conn,district,mandal))

    elif crops:
        return(get_details_by_crop(conn,crops))

    else:
        pass

def farmer_info(username):
    # result=farmer_details(conn,username)
    per=list(map(str,get_user_personal_details(conn,username)))
    agr=list(map(str,get_user_agro_details(conn,username)))
    cro=list(map(str,get_user_crop_details(conn,username)))
    return([per,agr,cro])
    


if __name__=="__main__":
    # farmer_search(range1=1,range2=2,district="Krishna",mandal="Kankipadu")
    farmer_info('xxxxx00002@24302')