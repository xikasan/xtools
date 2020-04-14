# coding: utf-8

from enum import Enum


class pycolor(Enum):

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RETURN = '\033[07m'  # 反転
    ACCENT = '\033[01m'  # 強調
    FLASH = '\033[05m'  # 点滅
    RED_FLASH = '\033[05;41m'  # 赤背景+点滅
    END = '\033[0m'

    def __init__(self, val):
        self._val = val

    def __repr__(self):
        return self._val

    def __str__(self):
        return self._val

    @classmethod
    def get(cls, obj):
        if isinstance(obj, cls):
            return obj
        if isinstance(obj, str):
            obj = str.upper(obj)
            for c in cls:
                if c.name == obj:
                    return c
        raise ValueError("Given" + obj + "is not found")


def print_message(kind, content, value=None, color=None):
    msg = "" if color is None else str(pycolor.get(color))
    msg += "[{}] ".format(kind)
    msg += str(content)
    msg += "" if value is None else (": " + str(value))
    msg += "" if color is None else str(pycolor.END)
    print(msg)


def info(content, value=None):
    print_message("info", content, value=value)


def debug(content, value=None, color="yellow"):
    print_message("debug", content, value=value, color=color)


def error(content, value=None, color="red"):
    print_message("error", content, value=value, color=color)


if __name__ == '__main__':
    x = 1e+3
    info("variable", x)
    debug("variable", x)
    error("variable", x)
