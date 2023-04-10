## 北航校园网登陆脚本
### 1.用法简介

脚本支持三种认证方式
- 文件输入账号密码信息
- 命令行输入参数
- 运行动态输入参数

### 2.参数介绍
#### 2.1文件输入认证
需要将账号和密码分行写入到user_info.txt文件，格式如下所示
```python
[username]
[password]
```
命令行运行
```python
python login.py [option]
```
~~这里的option参数支持如下所示的任意数字和字符串~~

由于api更改，当前仅支持0和3参数
```python
{"0":"login", "1":"logout", "2":"logout_all", "3":"check_online"}
```

#### 2.2命令行输入参数
需当不存在user_info.txt文件时，要按照如下格式运行程序
```python
python login.py [option] [username] [password]
```

#### 2.3运行动态输入参数
当不存在命令行参数和user_info.txt文件时，执行如下命令将会主动提示输入账号和密码
```python
python login.py [option]
```

### 3.参考脚本
[ywz978020607](https://github.com/ywz978020607/History/tree/master/cv%E7%A0%94%E7%A9%B6%E7%94%9F%E6%97%A5%E5%B8%B8Lab/pySrun4k_BeihangLogin-master)





