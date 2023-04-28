# 开发起因：串口调试工具，在串口断开后需要重新选择进行连接，这个过程会耗费一定的时间，而我们的模块上电就开始打印各种日志，导致部分日志丢失。所以就有了这个程序
# 开发环境 py3.8
# 依赖库 pyserial
import serial as pyserial
import time
from datetime import datetime
import sys
import json
import signal

# 连接的串口名
serial_port = 'COM17'
# 波特率
serial_baudrate = 115200
# 断开连接后的重连间隔(s)，太短电脑可能会蓝屏，注意！
interval_time = 1

# 打开本地文件
with open('config.json', 'r', encoding='utf-8') as f:
    # 通过load方法将文件内容读入到字典中
    data = json.load(f)

try:
    serial_port = data['serial_port']
    serial_baudrate = data['serial_baudrate']
    interval_time = data['interval_time']
    print("[当前配置]\n串口名:{}\n波特率:{}\n重连间隔(s):{}".format(serial_port, serial_baudrate, interval_time))
    f.close()
except Exception as e:
    print(e)
    print("解析config.json出错，请检查配置是否正确")
    sys.exit()

def get_current_date_string(format="%Y-%m-%d"):
    """返回当前日期的字符串表示形式，格式为 YYYY-MM-DD"""
    return datetime.today().strftime(format)

while True:
    try:
        ser = pyserial.Serial(serial_port, serial_baudrate)
        if ser.isOpen():
            print("串口已连接")
            break
    except pyserial.SerialException:
        print("串口连接失败，请检查串口是否正确连接")
        time.sleep(interval_time)

while True:
    try:
        # 忽略无法解码的字节
        data = ser.readline().decode('utf-8', 'ignore')
        print(data)
        file_path = "log-" + get_current_date_string() + ".txt"
        # 日志写入本地
        with open(file_path, 'a') as f:
            f.write(data)
        f.close()
    except pyserial.SerialException:
        print("串口断开，正在尝试重新连接", end="")
        while True:
            try:
                ser = pyserial.Serial(SERIAL_PORT, SERIAL_BAUDRATE)
                if ser.isOpen():
                    print("\n串口已重新连接")
                    break
            except pyserial.SerialException:
                print(".", end="", flush=True)
                time.sleep(interval_time)
