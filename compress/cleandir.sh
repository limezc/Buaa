#!/bin/bash

# 清理目录
function clean_dir() {
    local dir=$1

    # 判断dir是否为空
    if [ ! "$(ls -A $dir)" ]; then
        echo "Directory $dir is empty. Nothing to clean."
        exit 1
    fi

    # 清理目录
    rm -rf "$dir"/*
}


# 清理compress和decompress两个文件夹下的所有文件
clean_dir "compress_result"
clean_dir "decompress_result"

