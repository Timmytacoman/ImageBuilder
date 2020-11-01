from PIL import Image

# open image to process
im = Image.open(
    r'C:\Users\Timothy\PycharmProjects\misc_projects\img_to_blocks\images\unnamed (1).jpg')  # Can be many different formats.

# get width and height
width, height = im.size
# load all pixel rgbs
pix = im.load()


def get_distance(v1, v2):
    """math bruh"""
    x0, y0, z0 = v1
    ex, ey, ez = v2
    return ((ex - x0) ** 2 + (ey - y0) ** 2 + (ez - z0) ** 2) ** .5


def get_block_equivalence(values):
    """Find the corresponding block from a dictionary setup"""


    # Improvements coming
    dictionary = {
        (255, 0, 0): "REDSTONE_BLOCK",
        (0, 255, 0): "GRASS",
        (62, 187, 99): "GRASS",
        (0, 0, 255): "LAPIS_BLOCK",
        (255, 255, 255): "IRON_BLOCK",
        (0, 255, 255): "DIAMOND_BLOCK",
        (153, 204, 255): "MELON_BLOCK",
        (128, 0, 0): "NETHERRACK",
    }

    smallest = 1e5
    for i in dictionary:
        dist = get_distance(values, i)
        if dist < smallest:
            smallest = dist
            key = i
    return dictionary[key]


# scan each pixel in image
s = ""
for y in range(height):
    for x in range(width):
        s += get_block_equivalence(pix[x, y]) + ", "

# chop off last ", "
s = s[:-2]

# write to file
file = open("block_data.txt", "w")
file.write(s)
file.close()
