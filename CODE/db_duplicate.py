from db_connect import connect
import random,json
from panda_main import main
from db_user import user_details

c=connect()
with open('datasets/dat.json','r') as f:
    mand_list=json.load(f)
dist_list=list(mand_list.keys()) 

data=main()

def main():
    PhNo=8712324300
    crops=data['crop'].unique()
    val={}
    for i in range(1,30001):
        PhNo=PhNo+1
        val['Name']='xxxxx'+str(i).zfill(5)
        val['Age']=random.randint(30,60)
        val['PhNo']=str(PhNo)
        val['Address']='xxxxx street'
        val['district']=random.choice(dist_list)
        val['mandal']=random.choice(mand_list[val['district']])
        val['place']=val['mandal']
        val['identity']=random.choice(["Own_Land","Lease_Land"])
        val['landarea']=round(random.uniform(1,5),2)
        val['culture']=random.choice(['Monoculture','Polyculture'])
        val['cropkind']=random.choice(['cash','food','horticulture','plantation'])
        val['crop_select']=random.choice(crops)
        val['date1']='1/04/2020'
        val['crop1']=random.choice([val['crop_select'],random.choice(crops)])
        production=list(data[data['crop']==val['crop1']]['per(1acre)'])
        val['prod1']=round(val['landarea']*random.choice(production),2)
        val['date2']='1/09/2019'
        val['crop2']=random.choice([val['crop_select'],val['crop1'],random.choice(crops)])
        production=list(data[data['crop']==val['crop2']]['per(1acre)'])
        val['prod2']=round(val['landarea']*random.choice(production),2)
        val['date3']='1/03/2019'
        val['crop3']=random.choice([val['crop_select'],val['crop1'],val['crop2'],random.choice(crops)])
        production=list(data[data['crop']==val['crop3']]['per(1acre)'])
        val['prod3']=round(val['landarea']*random.choice(production),2)
        user_details(val)

if __name__ == "__main__":
    main()