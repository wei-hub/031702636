# -*- coding: utf-8 -*-
import re
import json

#add = '1!小陈,新疆维吾尔自治区阿克苏凤岗13965231525镇凤平路13号.'
#add = '2!李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层.'
#add = '1!张三,福建福州闽13599622362侯县上街镇福州大学10#111.'
#add = '2!王五,福建省福州市鼓楼县五一北路18960221533123号福州鼓楼县医院.'
#add = '3!小美,北京市东15822153326城区交道口东大街1号北京市东城区人民法院.'
#add = '1!娄伤囚,浙江省杭州市丰泽区所前镇袄庄陈村13592755594工业园区5号楼.'
add = input() #输入数据
name = re.search('!(.*?),',add)
name = re.sub(r'\!|\,','',name.group())#把名字提取出来
tele = re.search('\d\d\d+',add).group(); #把电话号码提取出来
#print(name),print(tele)
dict = {'姓名':name,'手机':tele}
#print(dict)
add1 = re.sub('(.*?),|\.|(\d{11})','',add) #把地址提取出来
#print(add1)
ans = []
list = ['北京市','天津市','上海市','上海市']
#判断是否为直辖市
if((add1[0:2]+'市') in list):
    ans.append(add1[0:2])
    ans.append(add1[0:2]+'市')
    if(add1[2] == '市'):  add1 = re.sub(r'^.{3}','',add1)
    else :  add1 = re.sub(r'^.{2}','',add1)
    
    #判断区级城市
    if('区' in add1 or '县' in add1):#无区字缺失
        area = re.match(r'.*?区|县',add1)
        ans.append(area.group())
        add1 = re.sub(area.group(),'',add1,1)
        #print(ans)
        #print(add1)
    else:
        if('区' in add1):
            area = add1[0:2]+'区'
            #print(city)
            ans.append(area)
            add1=re.sub('(^.{2})','',add1,1)
            #print(add1)
        elif('县' in add1):
            area = add1[0:2]+'县'
            #print(city)
            ans.append(area)
            add1=re.sub('(^.{2})','',add1,1)
            #print(add1)

    #判断街道/镇/乡
    if('街道' in add1 or '镇' in add1 or '乡' in add1 or  '口' in add1):
        if('口' in add1):
            town = re.match('.*口',add1)
            ans.append(town.group()+'街道')
            #print(ans)
            #print(add1)
        else:
            town = re.match('.*?[镇|乡|街道]',add1)
            ans.append(town.group())
            #print(ans)
            add1 = re.sub(town.group(),'',add1,1)
            #print(add1)

    else:
        ans.append('')
        #print(ans)

    flag = add[0]
    if(flag == '1'):
        ans.append(add1)
        #print(ans)
    
    elif(flag == '2' or flag == '3'):
        if('道' in add1 or '镇' in add1 or '乡' in add1 or '路' in add1 or '巷' in add1 or '街' in add1):
            load = re.match('.*?[道|路|巷|街]',add1)
            ans.append(load.group())
            #print(ans)
            add1 = re.sub(load.group(),'',add1,1)
            #print(add1)
        else:
            ans.append('')

        if( '号' in add1):
            num = re.match('.*?[号]',add1)
            ans.append(num.group())
            #print(ans)
            add1 = re.sub(num.group(),'',add1,1)
            #print(add1)

        else:
            ans.append('')
        ans.append(add1)

#非直辖市
else:
    if('自治区' in add1):
        zizi = re.match(r'.*自治区',add1)
        ans.append(zizi.group())
        add1 = re.sub(zizi.group(),'',add1,1)
    elif('省' in add1):#无省字缺失
        province = re.match(r'.*省',add1)
        #print(province)
        ans.append(province.group())
        add1 = re.sub(province.group(),'',add1,1)
        #print(ans)
        #print(add1)
    else:
        if('黑龙江' in add1):
            province = '黑龙江省'
            ans.append(province)
            add1=re.sub('黑龙江','',add1)
            #print(add1)
            #print(ans)
        else:
            province = add1[0:2]+'省'
            ans.append(province)
            add1=re.sub('(^.{2})','',add1)
            #print(add1)
            #print(ans)
    
    #判断市级城市
    if('市' in add1):#无市字缺失
        city = re.match(r'.*?市',add1)
        ans.append(city.group())
        add1 = re.sub(city.group(),'',add1,1)
        #print(ans)
        #print(add1)
    else:
        if(add1[0:3] in ['马鞍山','六盘水','秦皇岛','石家庄','驻马店' ,'三门峡','哈尔滨' ,'牡丹江','佳木斯','七台河','双鸭山','梅河口','连云港','张家港','井冈山','景德镇','海拉尔','石嘴山','青铜峡','攀枝花','日喀则','吐鲁番','石河子','库尔勒','阿克苏']):
            city = add1[0:3]+'市'
            #print(city)
            ans.append(city)
            add1=re.sub('(^.{3})','',add1)
            #print(add1)
        else :
            city = add1[0:2]+'市'
            #print(city)
            ans.append(city)
            add1=re.sub('(^.{2})','',add1,1)
            #print(add1)

    #判断区/县/县级市
    if('区' in add1 or '县' in add1 or '市' in add1):#无缺失
        country = re.match(r'.*?[区|县|市]',add1)
        ans.append(country.group())
        #print(ans)
        add1 = re.sub(country.group(),'',add1,1)
        #print(add1)
    else:
        ans.append('')
        #print(ans)

    #判断街道/镇/乡
    if('街道' in add1 or '镇' in add1 or '乡' in add1 or '巷' in add1 or '道' in add1):
        town = re.match('.*[街道|镇|乡|道]',add1)
        ans.append(town.group())
        #print(ans)
        add1 = re.sub(town.group(),'',add1,1)
        #print(add1)

    else:
        ans.append('')
        #print(ans)

    #判断详细地址
    flag = add[0]
    if(flag == '1'):
        ans.append(add1)
        #print(ans)
    
    elif(flag == '2' or flag == '3'):
        if('街道' in add1 or '镇' in add1 or '乡' in add1 or '路' in add1 or '巷' in add1 or '街' in add1):
            load = re.match('.*?[街道|路|巷|街]',add1)
            ans.append(load.group())
            #print(ans)
            add1 = re.sub(load.group(),'',add1,1)
            #print(add1)
        else:
            ans.append('')

        if( '号' in add1):
            num = re.match('.*?[号]',add1)
            ans.append(num.group())
            #print(ans)
            add1 = re.sub(num.group(),'',add1,1)
            #print(add1)

        else:
            ans.append('')
        ans.append(add1)
        
dict['地址'] = ans
#print(dict)
print(json.dumps(dict))