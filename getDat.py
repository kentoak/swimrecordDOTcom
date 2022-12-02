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
def getDat(swimmerName,waterWay,swimmerSex,distance,swimmingStyle):
    nameList=[]
    waterWayAll=False
    distanceAll=False
    styleAll=False
    if waterWay=="ALL":
        waterWayAll=True
    else:
        waterway_code=get_keys_from_value(waterway_code_dict,waterWay)
    if distance=="ALL":
        distanceAll=True
    else:
        distance_code=get_keys_from_value(distance_code_dict,distance)
    if swimmingStyle=="ALL":
        styleAll=True
    else:
        swimming_style_code=get_keys_from_value(swimming_style_code_dict,swimmingStyle)
    gender_code=get_keys_from_value(gender_code_dict,swimmerSex)
    #for year in range(2008,2023):
    if waterWayAll:
        for waterway_code in range(1,3):
            if styleAll:
                for swimming_style_code in range(1,6):
                    if distanceAll:
                        for distance_code in range(2,8):
                            #print("1")
                            for year in range(2008,2023):
                                jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                                path='./concated/'+str(year)+'_rank200/'+jname+".json"
                                if os.path.exists(path):
                                    with open(path) as f:
                                        s = f.read()
                                        dat = dict(json.loads(s))['data']
                                        for k,i in enumerate(dat):
                                            name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                            info=i["record"]
                                            info["ランク"]=i["ranking"]
                                            info["記録"]=i["record"]["record"]
                                            info["日付"]=i["record"]["achieve_date"]
                                            info["年度"]=year
                                            info["大会名"]=i["achieved_game"]["game_name"]
                                            info['swimmerSex']=str(gender_code_dict[gender_code])
                                            info['waterWay']=str(waterway_code_dict[waterway_code])
                                            info['distance']=str(distance_code_dict[distance_code])
                                            info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                            info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                            info['所属']=i["swimmers"]['entry_group']['name']
                                            if name==swimmerName:
                                                nameList.append(info)
                    else:
                        #print("2")
                        for year in range(2008,2023):
                            jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                            path='./concated/'+str(year)+'_rank200/'+jname+".json"
                            if os.path.exists(path):
                                with open(path) as f:
                                    s = f.read()
                                    dat = dict(json.loads(s))['data']
                                    for k,i in enumerate(dat):
                                        name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                        info=i["record"]
                                        info["ランク"]=i["ranking"]
                                        info["記録"]=i["record"]["record"]
                                        info["日付"]=i["record"]["achieve_date"]
                                        info["年度"]=year
                                        info["大会名"]=i["achieved_game"]["game_name"]
                                        info['swimmerSex']=str(gender_code_dict[gender_code])
                                        info['waterWay']=str(waterway_code_dict[waterway_code])
                                        info['distance']=str(distance_code_dict[distance_code])
                                        info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                        info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                        info['所属']=i["swimmers"]['entry_group']['name']
                                        if name==swimmerName:
                                            nameList.append(info)
            else:
                if distanceAll:
                    #print("3")
                    for distance_code in range(2,8):
                        for year in range(2008,2023):
                            jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                            path='./concated/'+str(year)+'_rank200/'+jname+".json"
                            if os.path.exists(path):
                                with open(path) as f:
                                    s = f.read()
                                    dat = dict(json.loads(s))['data']
                                    for k,i in enumerate(dat):
                                        name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                        info=i["record"]
                                        info["ランク"]=i["ranking"]
                                        info["記録"]=i["record"]["record"]
                                        info["日付"]=i["record"]["achieve_date"]
                                        info["年度"]=year
                                        info["大会名"]=i["achieved_game"]["game_name"]
                                        info['swimmerSex']=str(gender_code_dict[gender_code])
                                        info['waterWay']=str(waterway_code_dict[waterway_code])
                                        info['distance']=str(distance_code_dict[distance_code])
                                        info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                        info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                        info['所属']=i["swimmers"]['entry_group']['name']
                                        if name==swimmerName:
                                            nameList.append(info)
                else:
                    #print("4")
                    for year in range(2008,2023):
                        jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                        path='./concated/'+str(year)+'_rank200/'+jname+".json"
                        if os.path.exists(path):
                            with open(path) as f:
                                s = f.read()
                                dat = dict(json.loads(s))['data']
                                for k,i in enumerate(dat):
                                    name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                    info=i["record"]
                                    info["ランク"]=i["ranking"]
                                    info["記録"]=i["record"]["record"]
                                    info["日付"]=i["record"]["achieve_date"]
                                    info["年度"]=year
                                    info["大会名"]=i["achieved_game"]["game_name"]
                                    info['swimmerSex']=str(gender_code_dict[gender_code])
                                    info['waterWay']=str(waterway_code_dict[waterway_code])
                                    info['distance']=str(distance_code_dict[distance_code])
                                    info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                    info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                    info['所属']=i["swimmers"]['entry_group']['name']
                                    if name==swimmerName:
                                        nameList.append(info)
    else:
        if styleAll:
            for swimming_style_code in range(1,6):
                if distanceAll:
                    #print("5")
                    for distance_code in range(2,8):
                        for year in range(2008,2023):
                            jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                            path='./concated/'+str(year)+'_rank200/'+jname+".json"
                            if os.path.exists(path):
                                with open(path) as f:
                                    s = f.read()
                                    dat = dict(json.loads(s))['data']
                                    for k,i in enumerate(dat):
                                        name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                        info=i["record"]
                                        info["ランク"]=i["ranking"]
                                        info["記録"]=i["record"]["record"]
                                        info["日付"]=i["record"]["achieve_date"]
                                        info["年度"]=year
                                        info["大会名"]=i["achieved_game"]["game_name"]
                                        info['swimmerSex']=str(gender_code_dict[gender_code])
                                        info['waterWay']=str(waterway_code_dict[waterway_code])
                                        info['distance']=str(distance_code_dict[distance_code])
                                        info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                        info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                        info['所属']=i["swimmers"]['entry_group']['name']
                                        if name==swimmerName:
                                            nameList.append(info)
                else:
                    #print("6")
                    for year in range(2008,2023):
                        jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                        path='./concated/'+str(year)+'_rank200/'+jname+".json"
                        if os.path.exists(path):
                            with open(path) as f:
                                s = f.read()
                                dat = dict(json.loads(s))['data']
                                for k,i in enumerate(dat):
                                    name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                    info=i["record"]
                                    info["ランク"]=i["ranking"]
                                    info["記録"]=i["record"]["record"]
                                    info["日付"]=i["record"]["achieve_date"]
                                    info["年度"]=year
                                    info["大会名"]=i["achieved_game"]["game_name"]
                                    info['swimmerSex']=str(gender_code_dict[gender_code])
                                    info['waterWay']=str(waterway_code_dict[waterway_code])
                                    info['distance']=str(distance_code_dict[distance_code])
                                    info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                    info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                    info['所属']=i["swimmers"]['entry_group']['name']
                                    if name==swimmerName:
                                        nameList.append(info)
        else:
            if distanceAll:
                #print("7")
                for distance_code in range(2,8):
                    for year in range(2008,2023):
                        jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                        path='./concated/'+str(year)+'_rank200/'+jname+".json"
                        if os.path.exists(path):
                            with open(path) as f:
                                s = f.read()
                                dat = dict(json.loads(s))['data']
                                for k,i in enumerate(dat):
                                    name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                    info=i["record"]
                                    info["ランク"]=i["ranking"]
                                    info["記録"]=i["record"]["record"]
                                    info["日付"]=i["record"]["achieve_date"]
                                    info["年度"]=year
                                    info["大会名"]=i["achieved_game"]["game_name"]
                                    info['swimmerSex']=str(gender_code_dict[gender_code])
                                    info['waterWay']=str(waterway_code_dict[waterway_code])
                                    info['distance']=str(distance_code_dict[distance_code])
                                    info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                    info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                    info['所属']=i["swimmers"]['entry_group']['name']
                                    if name==swimmerName:
                                        nameList.append(info)
            else:
                #print("8")
                for year in range(2008,2023):
                    jname=str(year)+"_"+str(gender_code_dict[gender_code])+"_"+str(waterway_code_dict[waterway_code])+"_"+str(distance_code_dict[distance_code])+"_"+str(swimming_style_code_dict[swimming_style_code])+"_200all"
                    path='./concated/'+str(year)+'_rank200/'+jname+".json"
                    if os.path.exists(path):
                        with open(path) as f:
                            s = f.read()
                            dat = dict(json.loads(s))['data']
                            for k,i in enumerate(dat):
                                name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                                info=i["record"]
                                info["ランク"]=i["ranking"]
                                info["記録"]=i["record"]["record"]
                                info["日付"]=i["record"]["achieve_date"]
                                info["年度"]=year
                                info["大会名"]=i["achieved_game"]["game_name"]
                                info['swimmerSex']=str(gender_code_dict[gender_code])
                                info['waterWay']=str(waterway_code_dict[waterway_code])
                                info['distance']=str(distance_code_dict[distance_code])
                                info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                                info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                                info['所属']=i["swimmers"]['entry_group']['name']
                                if name==swimmerName:
                                    nameList.append(info)
    # nameDict={}
    # nameDict[swimmerName]=nameList
    #print("nameList",nameList)
    return nameList



###これ使わない
def openFile(swimmerName,jname,year,gender_code,waterway_code,distance_code,swimming_style_code):
    path='./concated/'+str(year)+'_rank200/'+jname+".json"
    if os.path.exists(path):
        #print(path)
        with open(path) as f:
            s = f.read()
            dat = dict(json.loads(s))['data']
            for k,i in enumerate(dat):
                #print(i["swimmers"]["swimmer_name"])
                name=i["swimmers"]["swimmer_name"].replace('　', '').replace(' ', '')
                info=i["record"]
                info["ランク"]=i["ranking"]
                info["記録"]=i["record"]["record"]
                info["日付"]=i["record"]["achieve_date"]
                info["年度"]=year
                info["大会名"]=i["achieved_game"]["game_name"]
                info['swimmerSex']=str(gender_code_dict[gender_code])
                info['waterWay']=str(waterway_code_dict[waterway_code])
                info['distance']=str(distance_code_dict[distance_code])
                info['swimmingStyle']=str(swimming_style_code_dict[swimming_style_code])
                #print(i["record"]["achieve_date"])
                info["種目"]=str(distance_code_dict[distance_code])+" "+str(swimming_style_code_dict[swimming_style_code])
                info['所属']=i["swimmers"]['entry_group']['name']
                if name==swimmerName:
                    #print("info",info)
                    nameList.append(info)