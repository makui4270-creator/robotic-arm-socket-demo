"""
编写模拟Socket连接代码
"""
from pymycobot import MyCobotSocket
import socket
import errno

def socket_connect(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        print(f"✔连接成功：{ip}:{port}")
        s.close() #
        return True
    
    except socket.timeout:
        print(f"✘连接超时:IP地址错误或目标设备不在线 {ip}:{port}")
        return None
    
    except socket.gaierror:
        print(f"✘无网络/地址非法,无法解析IP地址:{ip}:{port}")
        return None

    except OSError as e:
        if e.errno == errno.ECONNREFUSED:
            print(f"✘端口{port}错误，连接被拒绝：{ip}:{port}")
        elif e.errno == errno.EHOSTUNREACH:
            print(f"✘主机路由不可达：{ip}:{port}")
        else:
            print(f"✘系统连接异常：{ip}:{port}，错误信息：{e}")
        return None
    
    except Exception as e:
        print(f"✘连接失败：{ip}:{port}，错误信息：{e}")
        return None


# ===机械臂控制业务代码===
if __name__ == "__main__":
    # ============【模式切换开关】============
    MODE = 1  # 1：本机仿真模式，2：真机局域网模式

    if MODE == 1:
        # 模式1：本机仿真模式
        print(f"当前模式：本机仿真模式")
        TEST_IP = "arm"
        TEST_PORT = 9094

    elif MODE == 2:
        # 模式2：真机局域网模式
        print(f"当前模式：真机局域网模式")
        TEST_IP = "192.168.1.100"
        TEST_PORT = 9094
    # =======================================

    check_ok = socket_connect(TEST_IP, TEST_PORT)

    if check_ok:
        mc = MyCobotSocket(TEST_IP, TEST_PORT)
        print(f"控制机械臂回零")
        mc.send_angles([0, 0, 0, 0, 0, 0], 20)
        res = mc.get_angles()
        print(f"机械臂角度：{res}")
    
    else:
        print(f"无法连接机械臂，请检查IP和端口是否正确，或者网络是否正常")


