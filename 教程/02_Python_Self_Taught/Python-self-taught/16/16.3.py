在命令行输入“pwd ~”，找到Home的绝对路径，
然后使用文本编辑器创建一个名为.profile的文件，在第一行输入“export $python_projects=[绝对路径]”，[绝对路径]由pwd命令打出。
再退出重新打开Bash，输入“echo $python_projects”即可打印该环境变量了。

2025.3.11晚20：40
完美完成第16章的挑战练习
以下是16.3的相关命令：
nano ~/.profile
export python_projects=/(这里我设置的目录是根目录，其实只要找到Ubuntu中Python文件的目录的绝对路径替换掉这里的根目录就满足题目要求了。)
Ctrl+X
Y
"Enter"键
source ~/.profile(为了使创建的环境变量在没有退出重新登录的情况下生效。)
cd $python_projects(这样就可以直接到达想要到达的根目录。)
pwd(用来检验是否真的到达了根目录。)
ls(也可以用ls命令打印出当前目录下含有的目录和文件夹名称来检验是否真的到达了根目录。)