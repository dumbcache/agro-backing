from panda_data import data
from datetime import date
import pandas as pd

def main(crop_data):

    """ yearwise production of different crops per acre """

    yearly_crops=crop_data[['year','season','area','district_name','production','crop']].groupby(["season",'year','district_name','crop']).mean()
    average_production=yearly_crops['production']/yearly_crops['area']
    average=pd.Series(average_production,name='per(1acre)')
    result=pd.concat([yearly_crops,average],axis=1)
    
    return(result)