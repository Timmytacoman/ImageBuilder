from PIL import Image


def get_distance(v1, v2):
    """math bruh"""
    x0, y0, z0 = v1
    ex, ey, ez = v2
    return ((ex - x0) ** 2 + (ey - y0) ** 2 + (ez - z0) ** 2) ** .5


def get_directory(path_to_file):
    """gets directory from rgb_block_data.csv"""
    file = open(path_to_file, "r")
    line_counter = 0
    dictionary = {}
    for line in file:
        if line_counter > 0:
            list_of_line = line.split(",")
            rgb = list_of_line[0].split(".")
            rgb = tuple(list(map(int, rgb)))

            if "\n" in list_of_line[1]:
                block = list_of_line[1][:-1]
            else:
                block = list_of_line[1]

            dictionary[rgb] = block

        else:
            line_counter = 1
    file.close()
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
        r'C:\Users\Timothy\PycharmProjects\misc_projects\img_to_blocks\images\chris_nelson-399x600.jpg')  # Can be many different formats.

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


def get_edu_def_for_java(path_to_file):
    """Make sure rgb_block_data.csv has an empty line at the bottom"""
    file = open(path_to_file, "r")
    writer = open("edu_generator.txt", "w")
    line_counter = 0
    for line in file:
        if line_counter > 0:
            list_of_line = line.split(",")
            block = list_of_line[1][:-1]
            text = f'edu.put("{block}", Material.{block});\n'
            writer.write(text)

        else:
            line_counter = 1

    file.close()
    writer.close()


if __name__ == "__main__":
    """Warning: must add new line at end of rgb_block_data.csv!!!"""
    write_block_data(scan())
    get_edu_def_for_java(r"C:\Users\Timothy\PycharmProjects\misc_projects\img_to_blocks\rgb_block_data.csv")
