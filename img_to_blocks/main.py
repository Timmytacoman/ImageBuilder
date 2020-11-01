from PIL import Image


def get_distance(v1, v2):
    """math bruh"""
    x0, y0, z0 = v1
    ex, ey, ez = v2
    return ((ex - x0) ** 2 + (ey - y0) ** 2 + (ez - z0) ** 2) ** .5


def get_directory(path_to_file):
    """gets directory from rgb_block_data.csv"""
    # TODO: replace shulker boxes
    file = open(path_to_file, "r")
    line_counter = 0
    dictionary = {}
    for line in file:
        if line_counter > 0:
            # search from back to front for ','
            # split into two parts
            comma_is_present = False
            counter = -1
            while not comma_is_present:
                char = line[counter]
                if char == ",":
                    break
                else:
                    counter -= 1

            # find rgb
            rgb = line[:counter - 1]
            placeholder = rgb.find("rgb")
            rgb = rgb[placeholder + 4:-1]
            tuple_of_rgb = tuple(map(int, rgb.split(',')))

            # find block and chop off new line at end
            block = line[counter + 1:-1]

            dictionary[tuple_of_rgb] = block

        else:
            line_counter = 1
    return dictionary


def get_block_equivalence(values, dictionary):
    """Find the corresponding block from a dictionary setup"""

    smallest = 1e5
    for i in dictionary:
        dist = get_distance(values, i)
        if dist < smallest:
            smallest = dist
            key = i
    return dictionary[key]


def scan():
    # open image to process
    im = Image.open(
        r'C:\Users\Timothy\PycharmProjects\misc_projects\img_to_blocks\images\unnamed (1).jpg')  # Can be many different formats.

    # get width and height
    width, height = im.size
    # load all pixel rgbs
    pix = im.load()

    # load rgb_block_data.csv directory
    directory = get_directory(r"C:\Users\Timothy\PycharmProjects\misc_projects\img_to_blocks\rgb_block_data.csv")

    # scan each pixel in image
    s = str(width) + ", " + str(height) + ", "
    for y in range(height):
        for x in range(width):
            s += get_block_equivalence(pix[x, y], directory) + ", "

    # chop off last ", "
    s = s[:-2]
    return s


def write_block_data(s):
    # write to file
    file = open("block_data.txt", "w")
    file.write(s)
    file.close()


if __name__ == "__main__":
    """Warning: must add new line at end of rgb_block_data.csv!!!"""
    write_block_data(scan())
