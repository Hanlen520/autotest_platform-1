# 来自https://testerhome.com/topics/15534

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
BOOTSTRAP_SERVE_LOCAL = True
db_host='192.168.231.1'
db_port='3306'
db_user='root'
db_password='123456'
database='test_auto_new'

# smtp 发送邮件相关配置：
is_email_enable = False   #发送邮件开关
flask_host = 'http://localhost:5000'  # 邮件中的报告链接会使用
smtp_server_host = 'smtp.163.com'  # 如使用其他的smtp 服务，请修改对应host 和端口
smtp_server_port = '25'
smtp_from_email = 'gaozuxin@yeah.net'   # 发送邮件的邮箱账号
smtp_default_to_email = '120983257@qq.com'   # 默认接收邮件的邮箱账号
smtp_server_user = smtp_from_email
smtp_server_password = 'password'     # 发送邮件的邮箱密码

# atx 配置
isUseATX=True
ATXHost = 'http://localhost:8000'