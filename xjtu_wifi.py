import requests
import time
import re
from encryption.srun_md5 import *
from encryption.srun_sha1 import *
from encryption.srun_base64 import *
from encryption.srun_xencode import *
header={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'
}
init_url="http://172.16.1.11/srun_portal_pc"
get_challenge_api="http://172.16.1.11/cgi-bin/get_challenge"

srun_portal_api="http://172.16.1.11/cgi-bin/srun_portal"
get_info_api="http://172.16.1.11/cgi-bin/rad_user_info?callback=jQuery112402301351940080697_1759812122119&_=1759812122120"
n = '200'
type = '1'
ac_id='1'
enc = "srun_bx1"

def get_chksum():
	chkstr = token+username
	chkstr += token+hmd5
	chkstr += token+ac_id
	chkstr += token+ip
	chkstr += token+n
	chkstr += token+type
	chkstr += token+i
	return chkstr
def get_info():
	info_temp={
		"username":username,
		"password":password,
		"ip":ip,
		"acid":ac_id,
		"enc_ver":enc
	}
	i=re.sub("'",'"',str(info_temp))
	i=re.sub(" ",'',i)
	return i
def init_getip():
    global ip
    init_res = requests.get(init_url, headers=header)
    print("初始化获取ip")
    print("初始化页面返回内容：", init_res.text)  # 打印返回内容以便调试

    # 尝试匹配 IP 地址
    ip_match = re.search(r'ip\s*:\s*\"(.*?)\"', init_res.text)
    if ip_match:
        ip = ip_match.group(1)
        print("ip:", ip)
    else:
        print("无法匹配到 IP 地址，请检查页面结构或返回内容！")
        exit(1)  # 如果无法获取 IP，终止程序
def get_token():
	# print("获取token")
	global token
	get_challenge_params={
		"callback": "jQuery112404953340710317169_"+str(int(time.time()*1000)),
		"username":username,
		"ip":ip,
		"_":int(time.time()*1000),
	}
	get_challenge_res=requests.get(get_challenge_api,params=get_challenge_params,headers=header)
	token=re.search('"challenge":"(.*?)"',get_challenge_res.text).group(1)
	print(get_challenge_res.text)
	print("token为:"+token)
def do_complex_work():
	global i,hmd5,chksum
	i=get_info()
	i="{SRBX1}"+get_base64(get_xencode(i,token))
	hmd5=get_md5(password,token)
	chksum=get_sha1(get_chksum())
	print("所有加密工作已完成")
def login():
	srun_portal_params={
	'callback': 'jQuery11240645308969735664_'+str(int(time.time()*1000)),
	'action':'login',
	'username':username,
	'password':'{MD5}'+hmd5,
	'ac_id':ac_id,
	'ip':ip,
	'chksum':chksum,
	'info':i,
	'n':n,
	'type':type,
	'os':'windows+10',
	'name':'windows',
	'double_stack':'0',
	'_':int(time.time()*1000)
	}
	# print(srun_portal_params)
	srun_portal_res=requests.get(srun_portal_api,params=srun_portal_params,headers=header)
	print(srun_portal_res.text)
if __name__ == '__main__':
	global username,password
	username=""##你的登陆账户
	password=""##你的上网登陆密码
	init_getip()
	get_token()
	do_complex_work()
	login()
	res=requests.get(get_info_api,headers=header)
	print(res.text)
