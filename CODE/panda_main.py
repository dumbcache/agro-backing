from panda_data import data
import panda_average_crops
import panda_average_crops_districts
import pandas as pd

def main():

    """ main data manipulation entry for the application """

    crop_data=data() 
    average_crops=panda_average_crops.main(crop_data)
    average_crops_districtwise=panda_average_crops_districts.main(crop_data)

    average_production=crop_data['production']/crop_data['area']
    average=pd.Series(average_production,name='per(1acre)')
    crop_data=pd.concat([crop_data,average],axis=1)

    return(crop_data)

if __name__=="__main__":
    main()