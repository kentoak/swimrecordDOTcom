# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, flash
from getSwimmer_male import getSwimmer_male
from getSwimmer_female import getSwimmer_female
from getGender import getGender
from getDistance import getDistance
from getSwimmingStyle import getSwimmingStyle
from getWaterway import getWaterway
from getDat import getDat
from get_All import get_All
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1203" #flashで要る

swimmer_male_list=getSwimmer_male()
swimmer_female_list=getSwimmer_female()
waterway_list=getWaterway()
gender_list=getGender()
distance_list=getDistance()
swimmingstyle_list=getSwimmingStyle()

# ホームページ
@app.route('/')
def index():
    return render_template('index.html', swimmer_male_list=swimmer_male_list, swimmer_female_list=swimmer_female_list, waterway_list=waterway_list, gender_list=gender_list, distance_list=distance_list, swimmingstyle_list=swimmingstyle_list)


# 入力値の表示ページ
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == 'POST':
        sex,swimmerName,waterWay,distance,swimmingStyle="","","","",""
        if request.form.get('submit_female'):
            sex="Women"
            swimmerName = request.form.getlist('swimmerName_female')
            #swimmerName = request.form.get('js-select2_2')
            waterWay = request.form.get('waterWay_female')
            distance = request.form.get('distance_female')
            swimmingStyle = request.form.get('swimmingStyle_female')
            print(swimmingStyle,swimmerName)
        elif request.form.get('submit_male'):
            sex="Men"
            swimmerName = request.form.getlist('swimmerName_male')
            waterWay = request.form.get('waterWay_male')
            distance = request.form.get('distance_male')
            swimmingStyle = request.form.get('swimmingStyle_male')
            print(swimmingStyle,swimmerName)
        # else:
        #     print("mmmmmmm")
        #     return render_template('index.html')
        if len(swimmerName)==0:
            flash("選手を選択してください。検索して候補を絞れます。", "failed")#flash(message, category='message')
            return render_template('index.html', swimmer_male_list=swimmer_male_list, swimmer_female_list=swimmer_female_list, waterway_list=waterway_list, gender_list=gender_list, distance_list=distance_list, swimmingstyle_list=swimmingstyle_list)
            
        res=""
        dfsflag=False
        if len(swimmerName)>0:
            for name in swimmerName:
                print(name)
                nameLists = getDat(name,waterWay,sex,distance,swimmingStyle)
                df=pd.DataFrame(nameLists, columns=['年度', '所属', '種目', '記録', "ランク", "日付", "大会名"])
                df=df.sort_values('年度', ascending=False)
                if not df.empty:
                    dfsflag=True
                    #print(type(render_template('result.html', swimmerName = swimmerName, waterWay = waterWay, swimmerSex = sex, distance = distance, swimmingStyle = swimmingStyle, dataframe = df.to_html(index=False))))
                    #res+=render_template('result.html', swimmerName = name, waterWay = waterWay, swimmerSex = sex, distance = distance, swimmingStyle = swimmingStyle, dataframe = df.to_html(index=False))
                    results = {}
                    #print(len(nameLists))
                    #for i in range(len(nameLists)-1,-1,-1):
                    for i in range(len(nameLists)):
                        nameList=nameLists[i]
                        #event.append(nameList['waterWay']+" "+nameList['swimmerSex']+" "+nameList['distance']+" "+nameList['swimmingStyle'])
                        results.setdefault(nameList['waterWay']+" "+nameList['swimmerSex']+" "+nameList['distance']+" "+nameList['swimmingStyle'], []).append(nameList)
                        #df=pd.DataFrame([nameList], columns=['year', 'group', 'record', "game", "date"])
                        df=pd.DataFrame(nameLists, columns=['年度', '所属', '種目', '記録', "ランク", "日付", "大会名"])
                        df=df.sort_values('年度', ascending=False)
                        #res+=render_template('result.html', swimmerName = name, waterWay = nameList['waterWay'], swimmerSex = nameList['swimmerSex'], distance = nameList['distance'], swimmingStyle = nameList['swimmingStyle'], dataframe = df.to_html(index=False))
                    #print("results",results)
                    for key,val in results.items():
                        #print(val)
                        df=pd.DataFrame(val, columns=['年度', '所属', '種目', '記録', "ランク", "日付", "大会名"])
                        df=df.sort_values('年度', ascending=False)
                        #print(df.to_html(index=False))
                        res+=render_template('result.html', swimmerName = name, waterWay = key.split()[0], swimmerSex = key.split()[1], distance = key.split()[2], swimmingStyle = key.split()[3], dataframe = df.to_html(index=False))
                        # print(nameList['waterWay'])
                        # print(nameList['swimmerSex'])
                        # print(nameList['distance'],nameList['swimmingStyle'])
                        # res+=render_template('result.html', swimmerName = name, waterWay = nameList['waterWay'], swimmerSex = nameList['swimmerSex'], distance = nameList['distance'], swimmingStyle = nameList['swimmingStyle'], dataframe = df.to_html(index=False))
        #return render_template('result.html', swimmer_name = swimmer_name, dataframe = nameDict)
        if not dfsflag:
            if len(swimmerName)>0:
                for name in swimmerName:
                    nameLists = get_All(name)
                    res+="存在していないため、全てを表示します"
                    for nameList in nameLists:
                        df=pd.DataFrame(nameLists, columns=['年度', '所属', '種目', '記録', "ランク", "日付", "大会名"])
                        df=df.sort_values('年度', ascending=False)
                        if not df.empty:
                            dfsflag=True
                        res+=render_template('result.html', swimmerName = name, waterWay = nameList['waterWay'], swimmerSex = nameList['swimmerSex'], distance = nameList['distance'], swimmingStyle = nameList['swimmingStyle'], dataframe = df.to_html(index=False))
        return res#render_template('result.html', swimmerName = swimmerName, waterWay = waterWay, swimmerSex = sex, distance = distance, swimmingStyle = swimmingStyle, dataframe = df.to_html(index=False))
    else:
        print("ssssssss")
        return render_template('index.html')

if __name__=='__main__':
    #app.debug=True
    app.run(debug=False, host='0.0.0.0', port=3000)#host='0.0.0.0'で外部に公開できる？
    #app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)
