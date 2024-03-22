import os

from PIL import Image


def get_next_square_size(pixel):
    for i in range(1, 11):
        if 2 ** i >= pixel:
            return 2 ** i


def convert(path):
    before = Image.open(path)
    size = get_next_square_size(max(before.size))
    if before.size[0] != before.size[1]:
        # 不是方形的图片，需要转换
        new_image = Image.new("RGBA", (size, size))
        center = size / 2.0
        new_image.paste(before, (int(center - before.size[0] / 2.0), int(center - before.size[1] / 2.0)))
        return new_image
    if before.size == size:
        # 符合原尺寸
        return before
    # 需要拉伸
    resized_image = before.resize((size,size),Image.NEAREST)
    return resized_image
    


def main():
    if not os.path.exists("origin"):
        os.mkdir("origin")
        print("请在./origin目录下放置需要转换的图片")
        return
    if not os.path.exists("result"):
        os.mkdir("result")
    for file_name in os.listdir("origin"):
        if file_name.endswith(".png"):
            new_image = convert("origin" + os.sep + file_name)
            new_image.save("result" + os.sep + file_name)
            print(f"转换了{file_name}")


if __name__ == "__main__":
    main()
