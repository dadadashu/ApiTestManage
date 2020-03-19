import gevent.monkey
import multiprocessing

"""
gunicorn的配置文件
"""
# gevent的猴子魔法 变成非阻塞
gevent.monkey.patch_all()

bind = '0.0.0.0:8080'

#日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
loglevel = 'debug'


#日志输出路径。执行脚本当前路径下的logs目录
accesslog = "./logs/access.log"
errorlog = './logs/error.log'

# 启动的进程数
# workers = multiprocessing.cpu_count() * 2 + 1
workers=1

worker_class = 'gunicorn.workers.ggevent.GeventWorker'
