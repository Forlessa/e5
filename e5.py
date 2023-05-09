import time
import subprocess

def focus_timer():
    print('Focus timer started. Press Ctrl+C to stop.')
    while True:
        try:
            # 设置25分钟倒计时
            for i in range(1500, 0, -1):
                minutes = i // 60
                seconds = i % 60
                # 格式化时间并清空屏幕
                timer = '{}:{:02d}'.format(minutes, seconds)
                subprocess.call('clear', shell=True)
                # 打印倒计时并睡眠1秒钟
                print(timer)
                time.sleep(1)
            # 25分钟结束后打印信息并设置5分钟休息
            message = 'Time is up! Take a break.'
            subprocess.call(['notify-send', message])
            for i in range(300, 0, -1):
                minutes = i // 60
                seconds = i % 60
                # 格式化时间并清空屏幕
                timer = '{}:{:02d}'.format(minutes, seconds)
                subprocess.call('clear', shell=True)
                # 打印休息倒计时和消息，并睡眠1秒钟
                print('{}\n{}'.format(message, timer))
                time.sleep(1)
        except KeyboardInterrupt:
            # 如果按下Ctrl+C，则退出程序
            print('Focus timer stopped.')
            break
