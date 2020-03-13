# coding:utf-8

import time
import unittest
from macaca import WebDriver
from retrying import retry

desired_caps = {
    #设置平台
    'platformName': 'android',
    #设置APK路径，可以是本地路径，也可以是下载链接
    'app': 'app-debug.apk',
}

server_url = {
    #设置服务器地址，这里是本地
    'hostname': 'localhost',
    #设置端口号
    'port': 3456
}


def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver


def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        #初始化WebDriver
        cls.driver.init()

    def test_01_play_video(self):
        #通过driver调用element_by_name方法获取view的实例，再通过实例对象执行点击事件
        self.driver \
            .element_by_name('打开视频播放页') \
            .click()
        print("打开视频播放页成功")

        time.sleep(10)

        #执行单击(100,100)坐标，唤起播放器控制界面
        self.driver \
            .touch('tap', {
            'x': 100,
            'y': 100
        })

        time.sleep(1)

        #执行element_by_xpath方法找到对应的view实例，然后触发点击
        #这里xpath的获取需要用到一个工具，下文会提到
        self.driver \
            .element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView[1]') \
            .click()

        print("切换至全屏播放成功")

        time.sleep(7)

        # self.driver \
        #     .touch('tap', {
        #     'x': 100,
        #     'y': 100
        # })

        #触发屏幕拖拽事件
        self.driver \
            .touch([
            {
                'type': 'drag',
                'fromX': 100,
                'fromY': 300,
                'toX': 400,
                'toY': 300,
                'steps': 200
            }, {
                'type': 'drag',
                'toX': 600,
                'toY': 100,
                'duration': 3
            }
        ])

        print("进度调整成功")

        time.sleep(3)

        #触发返回事件
        self.driver \
            .back()

        print("返回")

        time.sleep(3)

        self.driver \
            .back()

        print("返回")

        time.sleep(3)

        self.driver \
            .element_by_name('打开视频列表') \
            .click()

        print("打开视频列表")

        time.sleep(3)

        self.driver \
            .touch([
            {
                'type': 'drag',
                'fromX': 100,
                'fromY': 600,
                'toX': 100,
                'toY': 300,
                'steps': 200
            }, {
                'type': 'drag',
                'toX': 0,
                'toY': 100,
                'duration': 1
            }
        ])

        print("滚动视频列表")

        time.sleep(3)

        self.driver \
            .element_by_xpath(
            '//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]') \
            .click()

        print("开始播放")

        time.sleep(10)

        self.driver \
            .back()

        print("自动化测试完成，一片祥和~")

if __name__ == '__main__':
    unittest.main()
