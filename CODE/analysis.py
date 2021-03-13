from panda_data import data
import panda_main
import panda_average_crops
import panda_average_crops_districts
import panda_yearly_crops
import pandas as pd

def analysis(args):

    # args=[['xxxxx00125', '53', '8712324425', 'xxxxx street', 'ANDHRA PRADESH', 'Visakhapatnam', 'Thondur', 'xxxxx00125@24425'], ['xxxxx00125@24425', 'Thondur', 'Own_Land', '2.85', 'Polyculture', 'cash', 'Rice'], ['xxxxx00125@24425', '2020-04-01', 'Castor seed', '1.19', '2019-09-01', 'Mango', '14.28', '2019-03-01', 'Wheat', '0.85']]

    crop=args[1][6]
    district=args[0][5].upper()
    data=panda_main.main()

    """ ---yearly production of crop in respective district---  """

    crop_data=data[(data['crop']==crop) & (data['district_name']==district)]
    crops=crop_data[['year','season','area','district_name','production','crop','per(1acre)']].groupby(['year']).mean()
    average_point=crops['per(1acre)'].mean()
    stat1={}
    stat1['data']=list(crops['per(1acre)'])
    stat1['labels']=[*range(1,len(stat1['data'])+1)]
    stat1['threshold']=[average_point]*len(stat1['data'])
    # return(stat1)

    """ ---yearly production of crop in respective district---  """

    crop_data=data[(data['crop']==crop)]
    crops=crop_data[['year','season','area','district_name','production','crop','per(1acre)']].groupby(['year']).mean()
    average_point=crops['per(1acre)'].mean()
    stat2={}
    stat2['data']=list(crops['per(1acre)'])
    stat2['labels']=[*range(1,len(stat2['data'])+1)]
    stat2['threshold']=[average_point]*len(stat2['data'])

    """ ---area of crop in respective district---  """

    crop_data=data[(data['district_name']==district)]
    crops=crop_data[['year','season','area','district_name','production','crop','per(1acre)']].groupby(['crop']).mean()
    area=crops['area'].sum()
    top_area=crops['area'].nlargest(5)
    area_per=(top_area/area)*100
    others=100-((top_area/area)*100).sum()
    c=pd.concat([area_per,pd.Series([others],index=['Others'])])
    stat3={}
    stat3['data']=list(c.round(2))
    stat3['labels']=list(c.index)

    """ ---crop area in different districts---  """

    crop_data=data[(data['crop']==crop)]
    crops=crop_data[['year','season','area','district_name','production','crop','per(1acre)']].groupby(['district_name']).mean()
    area=crops['area'].sum()
    area_per=(crops['area']/area)*100
    stat41={}
    stat41['data']=list(area_per.round(2))
    stat41['labels']=list(area_per.index)

    production=crops['per(1acre)'].mean()
    stat42={}
    stat42['data']=list(crops['per(1acre)'].round(2))
    stat42['labels']=list(crops.index)
    stat42['threshold']=[production]*14
    # print(stat4)

    return(stat1,stat2,stat3,stat41,stat42)

if __name__=="__main__":
    # analysis()
    pass
