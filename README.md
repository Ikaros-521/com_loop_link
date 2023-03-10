# 前言

## 开发起因
串口调试工具，在串口断开后需要重新选择进行连接，这个过程会耗费一定的时间，而我们的模块上电就开始打印各种日志，导致部分日志丢失。所以就有了这个程序


## 功能介绍
基于python3实现监听指定端口，获取串口打印数据存入log.txt文件，并自动重连。    

## 开发环境
操作系统：win10  
语言：python3.8.15  
编辑器：VS Code  
依赖库：pyserial （pip install pyserial）  

## 目录结构
- config.json （配置文件）
- log.txt （日志文件）
- main.exe （编译打包好的程序）
- main.py （程序源码）
- package.json （程序打包的相关配置 auto-py-to-exe）

# 使用

## 1.配置
自行修改为合适的配置即可。
```
{
    // 连接的串口名
    "serial_port": "COM17",
    // 波特率
    "serial_baudrate": 115200,
    // 断开连接后的重连间隔(s)，太短电脑可能会蓝屏，注意！
    "interval_time": 1
}
```

## 2.运行
双击`main.exe`即可。  
或搭建环境，运行 `python main.py`。  

