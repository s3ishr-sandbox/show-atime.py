#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def get_attr(path, debug=False):
    '''ファイルの最終アクセス時刻とファイルサイズを出力する'''
    if debug:
        return (os.path.getatime(path), os.path.getsize(path), path)
    return (os.path.getatime(path), os.path.getsize(path))

def get_tree(root):
    '''root配下のファイルを列挙するジェネレーター'''
    for path, dirs, files in os.walk(root):
        for f in files:
            realpath = os.path.join(path, f)
            # シンボリックリンクを除外
            if not os.path.islink(realpath):
                yield realpath

if __name__ == '__main__':
    homedir = os.environ['HOME']
    for file in get_tree(homedir):
        print(get_attr(file))

