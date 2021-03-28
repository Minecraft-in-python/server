from sys import platform
import time

_have_color = None
try:
    from colorama import Fore, Style, init
    init()
except ModuleNotFoundError:
    _have_color = False
else:
    _have_color = True

def log_err(text):
    # 打印错误信息
    if _have_color:
        print('%s[ERR  %s]%s %s' % (Fore.RED, time.strftime('%H:%M:%S'), Style.RESET_ALL, text))
    else:
        print('[ERR  %s] %s' % (time.strftime('%H:%M:%S'), text))

def log_info(text):
    # 打印信息
    if _have_color:
        print('%s[INFO %s]%s %s' % (Fore.GREEN, time.strftime('%H:%M:%S'), Style.RESET_ALL, text))
    else:
        print('[INFO %s] %s' % (time.strftime('%H:%M:%S'), text))

def log_warn(text):
    # 打印警告信息
    if _have_color:
        print('%s[WARN %s]%s %s' % (Fore.YELLOW, time.strftime('%H:%M:%S'), Style.RESET_ALL, text))
    else:
        print('[WARN %s] %s' % (time.strftime('%H:%M:%S'), text))

def pos2str(position):
    # 将坐标转换为字符串
    return ' '.join([str(s) for s in position])

def search_mcpy():
    # 寻找文件存储位置
    _os = __import__('os')
    environ, path = _os.environ, _os.path
    if 'MCPYPATH' in environ:
        MCPYPATH = environ['MCPYPATH']
    elif platform == 'darwin':
        MCPYPATH = path.join(path.expanduser('~'), 'Library', 'Application Support', 'mcpy')
    elif platform.startswith('win'):
        MCPYPATH = path.join(path.expanduser('~'), 'mcpy')
    else:
        MCPYPATH = path.join(path.expanduser('~'), '.mcpy')
    return MCPYPATH

def str2pos(string, float_=False):
    # pos2str 的逆函数
    if float_:
        return tuple([float(i) for i in string.split(' ')])
    else:
        return tuple([int(float(i)) for i in string.split(' ')])

VERSION = {
        'major': 0,
        'minor': 3,
        'patch': 1,
        'str': '0.3.1'
    }
