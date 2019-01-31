# 数据库配置
DBtype =  '2'   # '1' : sqlite,  2: mysql
db_host='192.168.10.70'
db_port='3306'
db_user='root'
db_password='123456'
database='test_auto_new'
# database='earth_test'

# atx 配置
isUseATX=True
ATXHost = 'http://localhost:8000'

# 截图目录相关配置
import os,platform
currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)
if platform.system()=='Windows':
    logPath = currentPath + '\\log\\'
    reportPathWin = currentPath + '\\templates\\reports\\'
    unittestPathWin = currentPath + '\\test\\'
    screen_shot_path = currentPath + '\\static\\screenshot\\'
else:
    reportPathLinux =currentPath + '/templates/reports/'
    unittestPathLinux = currentPath + '/test/'
    logPath = currentPath + '/log/'
    screen_shot_path = currentPath +'/static/screenshot/'

# smtp 发送邮件相关配置：
is_email_enable = False   #发送邮件开关
flask_host = 'http://localhost:5000'  # 邮件中的报告链接会使用
smtp_server_host = 'smtp.163.com'  # 如使用其他的smtp 服务，请修改对应host 和端口
smtp_server_port = '25'
smtp_from_email = 'youraccount@163.com'   # 发送邮件的邮箱账号
smtp_default_to_email = 'youraccount@163.com'   # 默认接收邮件的邮箱账号
smtp_server_user = smtp_from_email
smtp_server_password = 'yourpassword'     # 发送邮件的邮箱密码

