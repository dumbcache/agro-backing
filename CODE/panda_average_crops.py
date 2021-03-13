from panda_data import data
from datetime import date
import pandas as pd

def main(crop_data):

    """ total average production of the differnt crops per acre """
   
    total_average=crop_data[['year','season','area','district_name','production','crop']].groupby(['season','crop']).mean()
    average_production=total_average['production']/total_average['area']
    average=pd.Series(average_production,name='per(1acre)')
    result=pd.concat([total_average,average],axis=1)
    
    return(result)