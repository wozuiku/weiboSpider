
import os
from absl import app, flags
import shutil
import sys
import logging
import logging.config
import json

#from . import，代表使用相对路径导入，即从当前项目中寻找需要导入的包或函数
from weibo_spider import config_util




FLAGS = flags.FLAGS
flags.DEFINE_string('config_path', None, 'The path to config.json.')

logging_path = os.path.split(
    os.path.realpath(__file__))[0] + os.sep + 'logging.conf'
logging.config.fileConfig(logging_path)
logger = logging.getLogger('spider')


class Spider:

    def __init__(self):

        print('init')



#单前导下划线，仅供内部使用，只作为程序员的提示
def _get_config():


    #realpath() 获得的是该方法所在的脚本的路径，__file__为内置属性
    #split()，去除文件名，保留路径
    #os.sep根据你所处的平台，自动采用相应的分隔符号，在Windows上，文件的路径分隔符是'\'，在Linux上是'/'

    src = os.path.split(os.path.realpath(__file__))[0] + os.sep + 'config_sample.json'

    #os.getcwd() 方法用于返回当前工作目录

    config_path = os.getcwd() + os.sep + 'config.json'

    print('config_path = '+config_path)

    #print(src)
    #print(config_path)


    #判断FLAGS是否已经配置了config_path
    #flags.DEFINE_string('config_path', None, 'The path to config.json.')，None说明没有配置

    if FLAGS.config_path:
        config_path = FLAGS.config_path


    #判断config_path这个路径是否有配置文件
    #os.path.isfile()用于判断某一对象(需提供绝对路径)是否为文件
    elif not os.path.isfile(config_path):
        print('elif')
        #shutil.copy(src, config_path)，将src复制到config_path
        shutil.copy(src, config_path)
        logger.info(u'请先配置当前目录(%s)下的config.json文件，'
                    u'如果想了解config.json参数的具体意义及配置方法，请访问\n'
                    u'https://github.com/dataabc/weiboSpider#2程序设置' %
                    os.getcwd())
        sys.exit()

    print('config_path2 = '+config_path)

    try:
        with open(config_path) as f:
            config = json.loads(f.read())
            return config

    except ValueError:
        logger.error(u'config.json 格式不正确，请访问 '
                     u'https://github.com/dataabc/weiboSpider#2程序设置')
        sys.exit()






def main(_):
    try:
        print('main')
        config = _get_config()
        config_util.validate_config(config)
        print(config)
    except Exception as e:
        print('main Exception')
        logger.exception(e)



if __name__ == '__main__':
    app.run(main)
