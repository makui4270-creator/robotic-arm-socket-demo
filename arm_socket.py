"""
编写模拟Socket连接代码
"""
import socket
import errno

def socket_connect(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        print(f"✔连接成功：{ip}:{port}")
        return s
    
    except socket.timeout:
        print(f"✘连接超时：{ip}:{port}")
        return None

    except OSError as e:
        if e.errno == errno.ECONNREFUSED:
            print(f"✘端口{port}错误，链接被拒绝：{ip}:{port}")
        elif e.errno == errno.EHOSTUNREACH:
            print(f"✘无网络,无法解析IP地址：{ip}:{port}")
        return None
    
    except Exception as e:
        print(f"✘连接失败：{ip}:{port}，错误信息：{e}")
        return None

TEST_IP = "192.168.1.100"
TEST_PORT = 9094
socket_connect(TEST_IP, TEST_PORT)

