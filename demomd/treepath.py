#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'SarcasMe'

import sys
from pathlib import Path

# p = Path('C:\\Users\Administrator\Documents\Tencent Files\961085397\FileRecv')
# print(p.name)
# print(p.relative_to(p.parent))

ignore_dir = ['.git']

tree_str = ''

def generate_tree(path_name, n=0):

    global tree_str

    if path_name.is_file():
        tree_str += '    |' * n + '-' * 4 + path_name.name + '\n'
    elif path_name.is_dir():
        #tree_str += '    |' * n + '-' * 4 + str(path_name.relative_to(path_name.parent)) + '\\' + '\n'
        tree_str += '    |' * n + '-' * 4 + str(path_name.name) + '\\' + '\n'
        for cp in path_name.iterdir():
            generate_tree(cp, n+1)

def save_file(tree, filename='tree.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(tree)


if __name__ == '__main__':

    # 命令参数个数为2并且目录存在存在
    if len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
    # 命令参数个数为3并且目录存在存在
    if len(sys.argv) == 3 and Path(sys.argv[1]).exists():
        generate_tree(Path(sys.argv[1]), 0)
        save_file(tree_str, sys.argv[2])
    else:
        generate_tree(Path.cwd())
    print(tree_str)