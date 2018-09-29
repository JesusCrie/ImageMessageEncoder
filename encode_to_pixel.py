from PIL import Image


def group(lst: list, n: int):
    return zip(*[lst[i::n] for i in range(n)])


def string_to_pixel(msg: str):
    if not len(msg) % 3 == 0:
        msg += (" " * (3 - len(msg) % 3))

    out = [ord(c) for c in msg]
    return tuple(group(out, 3))


def load_n_encode(path: str, message: str):
    img: Image.Image = Image.open(path)
    pix = img.load()
    pxs = string_to_pixel(message)

    for i in range(len(pxs)):
        px = pxs[i]

        line: int = int(i / img.size[0])
        col: int = i % img.size[0]

        pix[col, line] = px

    img.save(path)


def dump_image_string(path: str):
    img: Image.Image = Image.open(path)
    pix = img.load()

    print("\n".join(["".join(["".join([chr(c) for c in pix[col, line]]) for col in range(img.size[0])]) for line in
                     range(img.size[1])]))
