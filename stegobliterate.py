USAGE_MSG = "Usage: python3 stegobliterate.py <original image> <output filename>"

# list of tuples representing which bits to flip and the
# probabilities of each for any given channel of any given
# pixel with 0 being the least significant bit and 7 being
# the most significant bit
BIT_CHOICES = [(0, 0.5), (1, 0.3), (2, 0.2)]


if __name__ == "__main__":

    from PIL import Image
    from random import choices
    from sys import argv

    # argv[1] -> original image
    # argv[2] -> output filename

    # check for correct number of command line arguments
    if len(argv) != 3:
        print(f"Incorrect number of arguments!\n{USAGE_MSG}")
        exit()

    # read image data and information
    try:
        im = Image.open(argv[1])
    except FileNotFoundError:
        print(f"Specified file not found!\n{USAGE_MSG}")
        exit()
    im_bytes = list(im.tobytes())
    n = len(im_bytes)

    # decide which bits to flip in each byte of the image
    flip_bits = choices(
        [choice[0] for choice in BIT_CHOICES],
        weights=[choice[1] for choice in BIT_CHOICES],
        k=n
    )

    # flip chosen bits in image bytes
    for i in range(n):
        im_bytes[i] ^= 1 << flip_bits[i]

    # convert output back to image object
    output_image = Image.frombytes(im.mode, im.size, bytes(im_bytes))

    # write output image to given output filename
    output_image.save(argv[2])
    output_image.close()
    print("Done!")
