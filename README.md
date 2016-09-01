### feature

1. 免去编译之后的手工拷贝备份
2. 支持配置文件，保存请求地址和 CGI 目录，免去每次输入
3. 支持请求参数文件，可以同时保存多个 CGI 及其请求参数，
4. 带有参数文件的注释功能，可以注释掉不用的 CGI 或者请求参数

### todo

目前暂无

### finished

* 拥有灵活的配置文件，这里以 constants.py 存在
* 覆盖前选择备份功能
* 高亮显示功能
* 注释功能
* 增强配置参数检测

### 运行前

* 配置 constants 文件下的 constants.py
* 配置 params 文件夹下的 params.py

### 运行

> 需要 python 2.7，可能需要 root 权限

`sudo ython __main__.py`
