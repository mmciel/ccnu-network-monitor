from selenium import webdriver
from selenium.common import NoSuchElementException
from time import sleep
import time
import sys

from config import *
from logger import init_logger

# 获取日志对象
log = init_logger('ccnu-network', 'INFO', 'ccnu-network.log', 'INFO')
# 驱动
dr = None


def initDriver():
    """ 基于Edge浏览器 ，如果切换其他浏览器，请切换包和类"""
    from selenium.webdriver.edge.service import Service
    from selenium.webdriver.edge.options import Options
    chrome_options = Options()
    # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    # 隐藏滚动条
    chrome_options.add_argument('--hide-scrollbars')
    # 禁用插件
    chrome_options.add_argument('--disable-plugins')
    # 不加载图片
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 是否使用GUI
    if getHasGUI():
        chrome_options.add_argument('--headless')
    service = Service(getDriverPath())
    service.start()
    global dr
    dr = webdriver.ChromiumEdge(service=service, options=chrome_options)


def open_login_page():
    if dr is None:
        log.error("驱动运行失败")
        return
    dr.get('https://portal.ccnu.edu.cn')
    sleep(2)


def login():
    user, pw = getUserInfo()
    log.info("登录者:"+user)
    username = dr.find_element(value='username')
    username.clear()
    sleep(1)
    password = dr.find_element(value='password')
    password.clear()
    sleep(1)
    username.send_keys(user)
    sleep(1)
    password.send_keys(pw)
    sleep(1)
    submitBtn = dr.find_element(value='login-account')
    submitBtn.click()
    log.info("已提交登录信息")


def smart_sleep():
    """根据工作时间来睡眠"""
    low_power_start = "02:00:00"
    low_power_end = "09:30:00"
    low_power_start_time = time.strptime(low_power_start, "%H:%M:%S")
    low_power_end_time = time.strptime(low_power_end, "%H:%M:%S")
    now_time = time.strptime(time.strftime("%H:%M:%S", time.localtime()), "%H:%M:%S")
    if low_power_start_time <= now_time <= low_power_end_time:
        # 每15分钟检查一次网络
        sleep(60 * 15)
    else:
        # 每分钟检查一次网络
        sleep(60)


def process():
    log.info("正在初始化驱动...")
    initDriver()
    log.info("正在打开登录页...")
    open_login_page()
    log.info("进入网络监听轮询...")
    while True:
        log.info("刷新当前页...")
        dr.refresh()
        sleep(2)
        try:
            # 如果注销按钮不存在，说明没登录，此时抛出异常
            try:
                dr.find_element(value='logout')
                log.info("用户已登录!")
            except NoSuchElementException:
                log.info("用户未登录，开始登录...")
                login()
        except Exception:
            log.error("未知异常")
        smart_sleep()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        log.error("请按照python main.py username password的格式重新运行命令")
    else:
        un = sys.argv[1]
        pw = sys.argv[2]
        setUserInfo(un, pw)

        process()
