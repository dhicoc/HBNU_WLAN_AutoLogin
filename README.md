## 深澜认证协议,python模拟登录hbnu校园网（仅限湖北师范大学校园网）

- 根据大佬博客修改，原文在：https://blog.csdn.net/qq_41797946/article/details/89417722
- 1.对原来的jxnu_wifi.py进行了适应性修改，将认证地址改为172.16.1.11及其子域名；将username和password行的账号密码信息删除
- 2.在KIMI的帮助下修改了encryption系列文件的一个数组索引越界的一个错误
- 3.新增了检查网络是否正常连接的检查程序，添加了提示信息

---

## 如何使用

### 1.打开hbnu_wifi.py,安装必须的软件包，然后添加username和password行的账号密码参数,srun_md5.py,srun_xencode.py中都有需要填写账号密码参数的部分，请注意：xjtu_wifi.py在L97,L98分别填写用户名和密码,srun_md5.py在L6填写密码,srun_xencode.py在L72，填写账号和密码

### 2.若调试完成，可用pyintsaller -F -w hbnu_wifi.py的命令进行打包，生成exe文件也可使用

---

## Contribute Together

### 1.欢迎PR，感谢！

### 2.求star!!! QAQ
