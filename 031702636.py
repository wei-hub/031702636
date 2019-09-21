# -*- coding: utf-8 -*- 
import re
import json
#add = '1!小陈,新疆维吾尔自治区阿克苏凤岗13965231525镇凤平路13号.'
#add = '2!李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层.'
#add = '1!张三,福建福州闽13599622362侯县上街镇福州大学10#111.'
#add = '2!王五,福建省福州市鼓楼县五一北路18960221533123号福州鼓楼县医院.'
#add = '3!小美,北京市东15822153326城区交道口东大街1号北京市东城区人民法院.'
#add = '1!娄伤囚,浙江省杭州市丰泽区所前镇袄庄陈村13592755594工业园区5号楼.'
add = input()
flag = add[0]#难度级别
name = re.search('!(.*?),',add)
name = re.sub(r'\!|\,','',name.group())#把名字提取出来
tele = re.search('\d\d\d+',add).group(); #把电话号码提取出来
#print(name),print(tele)
dict = {'姓名':name,'手机':tele,"地址":[]}
#print(dict)
addD = re.sub('(.*?),|\.|(\d{11})','',add) #把地址提取出来
#output['姓名']=re.search(r'\d!(.*),',userInput).group(1)
#output['手机']=re.search(r'\d{11}',userInput).group()
list = ['北京市','天津市','上海市','上海市']
case1 = ['省',"(市|自治州)",'(县|区|市)','(镇|街道|乡)',]
case2 = ['省','(市|自治州)','(县|区|市)','(镇|街道|乡)','(街|路|巷)','号',]
case = locals() ['case' + flag]
ans = []
anl = []
add1 = addD
if((add1[0:2]+'市') in list):
    anl.append(add1[0:2])
    anl.append(add1[0:2]+'市')
    if(add1[2] == '市'):  add1 = re.sub(r'^.{3}','',add1)
    else :  add1 = re.sub(r'^.{2}','',add1)
    
    #判断区级城市
    if('区' in add1 or '县' in add1):#无区字缺失
        area = re.match(r'.*?区|县',add1)
        anl.append(area.group())
        add1 = re.sub(area.group(),'',add1,1)
        #print(add1)
    else:
        if('区' in add1):
            area = add1[0:2]+'区'
            #print(city)
            anl.append(area)
            add1=re.sub('(^.{2})','',add1,1)
            #print(add1)
        elif('县' in add1):
            area = add1[0:2]+'县'
            #print(city)
            anl.append(area)
            add1=re.sub('(^.{2})','',add1,1)
            #print(add1)

    #判断街道/镇/乡
    if('街道' in add1 or '镇' in add1 or '乡' in add1 or  '口' in add1):
        if('口' in add1):
            town = re.match('.*口',add1)
            anl.append(town.group()+'街道')
            
            #print(add1)
        else:
            town = re.match('.*?[镇|乡|街道]',add1)
            anl.append(town.group())
            
            add1 = re.sub(town.group(),'',add1,1)
            #print(add1)

    else:
        anl.append('')
        

    flag = add[0]
    if(flag == '1'):
        anl.append(add1)
        
    
    elif(flag == '2' or flag == '3'):
        if('道' in add1 or '镇' in add1 or '乡' in add1 or '路' in add1 or '巷' in add1 or '街' in add1):
            load = re.match('.*?[道|路|巷|街]',add1)
            anl.append(load.group())
            
            add1 = re.sub(load.group(),'',add1,1)
            #print(add1)
        else:
            anl.append('')

        if( '号' in add1):
            num = re.match('.*?[号]',add1)
            anl.append(num.group())
            
            add1 = re.sub(num.group(),'',add1,1)
            #print(add1)

        else:
            anl.append('')
        anl.append(add1)

for i in range(len(case)):
    ans = re.search(r'\w+?'+case[i],addD)
    if ans:
        addD = re.sub(ans.group(),'',addD)
        dict['地址'].append(ans.group())
    else:
        dict['地址'].append('')
dict['地址'].append(addD)
print(json.dumps(dict))#输出
#print(dict)
