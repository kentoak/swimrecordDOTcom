# def getSwimmer_female():
#     swimmer=["池江璃花子","今井月","松本信歩","二宮歌梨","大橋悠依"]
#     return swimmer

import os
import json
from flask_wtf import FlaskForm
from wtforms import SelectField

waterway_code_dict={1:"LCM",2:"SCM"}
gender_code_dict={1:"Men",2:"Women"}
distance_code_dict={1:"25M",2:"50M",3:"100M",4:"200M",5:"400M",6:"800M",7:"1500M"}
swimming_style_code_dict={1:"Fr",2:"Ba",3:"Br",4:"Fly",5:"IM",6:"FR",7:"MR"}

def getSwimmer_female():
    nameList=[]
    for year in range(2022,2007,-1):
        for waterway_code in range(1,3):
            for swimming_style_code in range(1,6):
                for distance_code in range(2,7):
                    gender_code=2
                    jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                    path='./concated/'+str(year)+'_rank200/'+jname+".json"
                    if os.path.exists(path):
                        with open(path) as f:
                            s = f.read()
                            dat = dict(json.loads(s))['data']
                            for k,i in enumerate(dat):
                                #print(i["swimmers"]["swimmer_name"])
                                name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                if name not in nameList:
                                    nameList.append(name)
    #nameList=["池江璃花子","今井月","二宮歌梨","松本信歩"]
    return nameList#swimmer