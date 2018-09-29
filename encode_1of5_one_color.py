from PIL import Image


def encode_1of5_shift_color(pix: dict, size: tuple, msg: str, offset: int = 5):
    chars = [ord(c) for c in msg]

    # write length in the first pixel
    le = len(msg)
    sizes = ((le & (0xff << 24)), (le & (0xff << 16)), (le & (0xff << 8)), (le & 0xff))
    pix[0, 0] = sizes

    for i in range(1, len(chars) + 1):
        line: int = int(i * offset / size[0]) * offset
        col: int = i * offset % size[0]

        ps = list(pix[col, line])

        ps[i % 3] = chars[i - 1]
        pix[col, line] = tuple(ps)


def load_n_encode(path: str, msg: str, offset: int = 5):
    img: Image.Image = Image.open(path).convert('RGBA')
    pix = img.load()

    if (img.height * img.width) < len(msg) * (offset ** 2):
        raise IndexError('Image too small')

    encode_1of5_shift_color(pix, img.size, msg, offset)
    img.save(path)


def decode(path: str, offset: int = 5):
    img: Image.Image = Image.open(path)
    pix = img.load()

    sizes = pix[0, 0]
    size = (sizes[0] << 24) | (sizes[1] << 16) | (sizes[2] << 8) | sizes[3]

    # for line in range(offset, size):
    #    for col in range(offset, size):
    #        i = line * img.width + col
    #        ch = chr(pix[col * offset, line * offset][i % 3])
    #        print(ch, end='')
    #    print()

    msg = ''
    for i in range(1, size + 1):
        line: int = int(i * offset / img.size[0]) * offset
        col: int = i * offset % img.size[0]

        msg += chr(pix[col, line][i % 3])
    print(msg)

    # print("\n".join(["".join(
    #    [chr(pix[col * offset, line * offset][(line * img.width + col) % 3]) for col in range(int(img.width / offset))])
    #    for line in range(int(img.height / offset))]))
