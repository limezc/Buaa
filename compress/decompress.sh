#!/bin/bash

# 解压缩
function decompress() {
    local input_dir=$1
    local output_dir=$2
    local zip=$3

    # 创建必要的目录
    mkdir -p "$output_dir"

    # 判断input_dir是否为空
    if [ ! "$(ls -A $input_dir)" ]; then
        echo "Directory $input_dir is empty. Please provide a non-empty directory."
        exit 1
    fi

    # 判断output_dir是否为空
    if [ "$(ls -A $output_dir)" ]; then
        echo "Directory $output_dir is not empty. Please provide an empty directory."
        exit 1
    fi

    # 根据zip参数决定是否进行tar解压缩
    if [ "$zip" = "true" ]; then
        # 合并分片文件并进行tar解压缩
        cat "$input_dir"/slice-* | tar --null -zxf - -C "$output_dir"
    else
        # 合并分片文件并进行tar解包
        cat "$input_dir"/slice-* | tar --null -xf - -C "$output_dir"
    fi
}

# 检查参数
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <compressed_directory> <decompressed_directory> <zip>"
    exit 1
fi

# 参数
COMPRESSED_DIR=$1
DECOMPRESSED_DIR=$2
ZIP=$3

# 执行解压缩操作
decompress "$COMPRESSED_DIR" "$DECOMPRESSED_DIR" "$ZIP"