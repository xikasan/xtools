# coding: utf-8

import os
import datetime


# path correction
def up_dir_path(path, num_hierarchy):
    if os.name == 'nt':
        temp = path.split('\\')
    else:
        temp = path.split('/')
    abs_path = os.path.join(*temp[:-num_hierarchy])
    dir_name = temp[-num_hierarchy]
    return abs_path, dir_name


def go_to_root(file_path, root_name, verbose=False):
    # doner the path(__file__) of override code of this method as argument parameter `file_path`
    # and the package name as `root_name`
    assert isinstance(file_path, str) and isinstance(root_name, str), "give file path and root name as type `str`"
    assert file_path.find(root_name) > 0,\
        "root name `{}` is not found in given file path `{}`".format(root_name, file_path)
    file_path.replace('\\', '/')
    pos_root = file_path.rfind("/"+root_name+"/") + len(root_name)
    root_path = file_path[:pos_root]
    root_path, _ = up_dir_path(root_path, 1)
    return root_path


def join(*args):
    return os.path.join(*args)


# directory generation
def makedirs(path, exist_ok=False):
    if not exist_ok and not os.path.exists(path):
        raise FileExistsError
    os.makedirs(path, exist_ok=exist_ok)


def generate_time_dir_path(path=None, format="%Y.%m.%d.%H%M%S"):
    if path is None:
        path = os.getcwd()
    now = datetime.datetime.now().strftime(format)
    return join(path, now)


def make_dirs_current_time(path=None, format="%Y.%m.%d.%H%M%S", exist_ok=True):
    path = generate_time_dir_path(path, format=format)
    makedirs(path, exist_ok)
    return path
