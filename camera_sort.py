#!/usr/bin/env python3.5
import os
import progressbar


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def move_file(src, dst):
    try:
        os.replace(src, dst)
    except FileExistsError:
        dst += '_copy'
        move_file(src, dst)


if __name__ == '__main__':
    src_dir = os.path.abspath(input("Enter source dir: "))
    dst_dir = "/home/admin/Pictures/Camera unsorted test"

    create_dir(dst_dir)

    bar = progressbar.ProgressBar()
    last_subdir = None

    for entry in bar(os.listdir(src_dir)):
        if entry.endswith('.jpg') or entry.endswith('.mp4'):
            subdir = entry[0:4] + '.' + entry[4:6] + '.' + entry[6:8]
            if subdir != last_subdir:
                last_subdir = subdir
                create_dir(os.path.join(dst_dir, subdir))

            src = os.path.join(src_dir, entry)
            dst = os.path.join(dst_dir, subdir, entry)
            move_file(src, dst)
