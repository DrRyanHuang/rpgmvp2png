import os
import sys


def decrypt_rpgmvp(input_file, output_file):
    # PNG文件的文件头
    png_header = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'

    # 读取输入文件的内容
    with open(input_file, 'rb') as f_in:
        data = f_in.read()

    # 写入输出文件,包括PNG文件头和原始数据(跳过前32个字节)
    with open(output_file, 'wb') as f_out:
        f_out.write(png_header)
        f_out.write(data[32:])


def decrypt_directory(directory):
    # 获取输入目录的基本名称
    base_dir = os.path.basename(directory)
    # 在当前工作目录下创建同名的输出目录
    output_dir = os.path.join(os.getcwd(), base_dir)

    # 遍历输入目录下的所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 如果文件扩展名为.rpgmvp,则进行解密
            if file.endswith('.rpgmvp'):
                # 构建输入文件的完整路径
                input_file = os.path.join(root, file)
                # 获取输入文件相对于输入目录的相对路径
                relative_path = os.path.relpath(input_file, directory)
                # 获取输出文件的子目录路径
                output_subdir = os.path.dirname(relative_path)
                # 构建输出文件的文件名(将扩展名改为.png)
                output_file = os.path.splitext(relative_path)[0] + '.png'

                # 构建输出文件的完整目录路径
                output_path = os.path.join(output_dir, output_subdir)
                # 创建输出文件的目录(如果不存在)
                os.makedirs(output_path, exist_ok=True)

                # 构建输出文件的完整路径
                output_file_path = os.path.join(
                    output_path, os.path.basename(output_file))
                # 调用decrypt_rpgmvp函数解密单个文件
                decrypt_rpgmvp(input_file, output_file_path)


if __name__ == '__main__':
    # 如果命令行参数为3个,则解密单个文件
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        decrypt_rpgmvp(input_file, output_file)
    # 如果命令行参数为2个,则解密整个目录
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        if os.path.exists(path):
            if os.path.isfile(path):
                print(f"Error: '{path}' is a file, not a directory.")
            else:
                decrypt_directory(path)
        else:
            print(f"Error: Path '{path}' does not exist.")
    # 如果命令行参数不正确,则打印使用说明
    else:
        print("Usage:")
        print("  For single file: python decrypt_rpgmvp.py input.rpgmvp output.png")
        print("  For entire directory: python decrypt_rpgmvp.py directory_path")
