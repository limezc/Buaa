#!/bin/bash

# 压缩并生成分片
function compress_and_split() {
    local input_dir=$1
    local output_dir=$2
    local max_slice_size=$3
    local zip=$4

    # 确保输出目录存在
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

    # 进入目录
    pushd "$input_dir" > /dev/null

    # 根据zip参数决定是否进行zip压缩
    if [ "$zip" = "true" ]; then
        # 生成tar压缩文件并分片
        find . -type f -print0 | tar --null -zcf - --files-from=- | split -d -a 3 -b "$max_slice_size" - "$output_dir/slice-"
    else
        # 生成tar打包文件并分片
        find . -type f -print0 | tar --null -cf - --files-from=- | split -d -a 3 -b "$max_slice_size" - "$output_dir/slice-"
    fi
    
    popd > /dev/null
}

# 检查参数
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <source_directory> <compressed_directory> <max_slice_size> <zip>"
    exit 1
fi

# 参数
SOURCE_DIR=$1
COMPRESSED_DIR=$2
MAX_SLICE_SIZE=$3
ZIP=$4

# 执行压缩并生成分片操作
compress_and_split "$SOURCE_DIR" "$COMPRESSED_DIR" "$MAX_SLICE_SIZE" "$ZIP"