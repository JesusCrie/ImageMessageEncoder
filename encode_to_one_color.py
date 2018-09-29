from PIL import Image


def encode_to_shift_color(pix: dict, size: tuple, msg: str):
    chars = [ord(c) for c in msg]

    for i in range(len(chars)):
        line: int = int(i / size[0])
        col: int = i % size[0]

        ps = list(pix[col, line])

        ps[i % 3] = chars[i]
        pix[col, line] = tuple(ps)


def load_n_encode(path: str, msg: str):
    img: Image.Image = Image.open(path)
    pix = img.load()

    if img.height * img.width < len(msg):
        raise IndexError('Image too small')

    encode_to_shift_color(pix, img.size, msg)
    img.save(path)


def decode(path: str):
    img: Image.Image = Image.open(path)
    pix = img.load()

    # for line in range(img.height):
    #    for col in range(img.width):
    #        i = line * img.width + col
    #        ch = chr(pix[col, line][i % 3])

    # print(["\n".join([chr(pix[col, line][(line * img.width + col) % 3]) for col in range(img.width)]) for line in
    #       range(img.height)])

    print("\n".join(
        ["".join([chr(pix[col, line][(line * img.width + col) % 3]) for col in range(img.width)]) for line in
         range(img.height)]))
