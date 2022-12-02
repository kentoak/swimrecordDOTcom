import json
from pprint import pprint 
from dictknife import deepmerge 
from collections import defaultdict
import os

waterway_code_dict={1:"LCM",2:"SCM"}
gender_code_dict={1:"Men",2:"Women"}
distance_code_dict={1:"25M",2:"50M",3:"100M",4:"200M",5:"400M",6:"800M",7:"1500M"}
swimming_style_code_dict={1:"Fr",2:"Ba",3:"Br",4:"Fly",5:"IM",6:"FR",7:"MR"}
def get_keys_from_value(d, val):
    keys=[k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None

#discribe=["","Men","SCM","200M","Fly"]

#swimmerName=discribe[0]
def get_All(swimmerName):
    nameList=[]
    for year in range(2008,2023):
        for gender_code in range(2,0,-1):
            for waterway_code in range(1,3):
                for swimming_style_code in range(5,0,-1):
                    for distance_code in range(7,1,-1):
                        jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                        path='./concated/'+str(year)+'_rank200/'+jname+".json"
                        if os.path.exists(path):
                            #print(path)
                            with open(path) as f:
                                s = f.read()
                                dat = dict(json.loads(s))['data']
                                for k,i in enumerate(dat):
                                    #print(i["swimmers"]["swimmer_name"])
                                    name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                    if name==swimmerName:
                                        #print(name)
                                        info=i["record"]
                                        # info["record"]=i["record"]["record"]
                                        # info["date"]=i["record"]["achieve_date"]
                                        # info["year"]=year
                                        # info["game"]=i["achieved_game"]["game_name"]
                                        info["ランク"]=i["ranking"]
                                        info["記録"]=i["record"]["record"]
                                        info["日付"]=i["record"]["achieve_date"]
                                        info["年度"]=year
                                        info["大会名"]=i["achieved_game"]["game_name"]
                                        #print(i["record"]["achieve_date"])
                                        info['所属']=i["swimmers"]['entry_group']['name']
                                        info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                        #print(info)
                                        info['swimmerSex']=str(gender_code_dict[gender_code])
                                        info['waterWay']=str(waterway_code_dict[waterway_code])
                                        info['distance']=str(distance_code_dict[distance_code])
                                        info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                        nameList.append(info)
    #print(nameList)
    return nameList



# if __name__ == '__main__':
#     get_All("瀬戸大也")
