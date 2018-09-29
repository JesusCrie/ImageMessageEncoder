from PIL import Image


def encode_to_alpha(pix: dict, size: tuple, msg: str):
    alphas = [ord(c) for c in msg]

    for i in range(len(alphas)):

        line: int = int(i / size[0])
        col: int = i % size[0]

        p = list(pix[col, line])
        if len(p) == 3:
            raise KeyError('This image doesn\' have an alpha channel !')

        p[3] = alphas[i]

        pix[col, line] = tuple(p)


def load_n_encode(path: str, msg: str):
    img: Image.Image = Image.open(path)
    pix = img.load()

    if img.height * img.width < len(msg):
        raise IndexError('Not enough pixels to store your message !')

    encode_to_alpha(pix, img.size, msg)
    img.save(path)


def decode(path: str):
    img: Image.Image = Image.open(path)
    pix = img.load()

    print("\n".join(["".join([chr(pix[col, line][3]) for col in range(img.size[0])]) for line in range(img.size[1])]))
