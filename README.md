## 深澜认证协议,python模拟登录XJTU校园网（仅限兴庆教学区XJTU_STU Wifi 对应认证页面IP为10.6.18.2）

- 根据大佬博客原文：https://blog.csdn.net/qq_41797946/article/details/89417722修改
- 1.对原来的jxnu_wifi.py进行了适应性修改，将认证地址改为10.6.18.2及其子域名；将username和password行的账号密码信息删除
- 2.在KIMI的帮助下修改了encryption系列文件的一个数组索引越界的一个错误
- 3.新增了检查网络是否正常连接的检查程序，添加了提示信息

---

## 如何使用

### 1.打开xjtu_wifi.py,安装必须的软件包，然后添加username和password行的账号密码参数

### 2.若调试完成，可用pyintsaller -F -w xjtu_wifi.py的命令进行打包，生成exe文件也可使用

### 3.非教学区的XJTU_STU对应的认证页面是10.6.21.2，不能简单地修改代码中的认证网址就能实现在10.6.21.2环境下的认证，其他版本可能会解决
