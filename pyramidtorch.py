"""
Format for rerefence

5:return {
 {["y"] = 1, ["x"] = 0, ["name"] = "default:snowblock", ["z"] = 0, ["param2"] = 1, ["param1"] = 7},
 {["y"] = 1, ["x"] = 0, ["name"] = "default:snowblock", ["z"] = 38, ["param2"] = 1, ["param1"] = 7},
 {["y"] = 1, ["x"] = 38, ["name"] = "default:snowblock", ["z"] = 38, ["param2"] = 1, ["param1"] = 7},
 {["y"] = 1, ["x"] = 38, ["name"] = "default:snowblick", ["z"] = 0, ["param2"] = 1, ["param1"] = 7}
}
"""


def get_element(key, value):
    """ Return Lua table element """

    _element = "[\"" + key + "\"] = " + str(value) + ", "

    return _element


def get_line(xyz, torch):
    """ Return Lua table line """

    _line = "{"
    _line += get_element('x', xyz[0])
    _line += get_element('y', xyz[1])
    _line += get_element('z', xyz[2])
    if torch:
        _line += "[\"name\"] = \"default:torch\", [\"param2\"] = 7, [\"param1\"] = 7}, "
    else:
        _line += "[\"name\"] = \"default:snowblock\", [\"param2\"] = 1, [\"param1\"] = 7}, "

    return _line


def pyramid(pyramid_height, only_torch=False):
    """ Build pyramind """

    node_position = []

    for i in range(pyramid_height):

        i_ = i + 1

        # Length
        length = i_ * 2 - 1
        print("length", length)

        # Y
        y = pyramid_height - i_
        print("y", y)

        # X (Z)
        x_0 = y
        x_e = y + length - 1
        if only_torch:
            y_ = y + 1
        else:
            y_ = y

        corner_00 = (x_0, y_, x_0)
        corner_0z = (x_0, y_, x_e)
        corner_x0 = (x_e, y_, x_0)
        corner_xz = (x_e, y_, x_e)

        node_position.append(corner_00)
        node_position.append(corner_0z)
        node_position.append(corner_x0)
        node_position.append(corner_xz)

        if only_torch == False:
            for j in range(x_0 + 1, x_e):
                print("j", j)
                side_00 = (x_0, y_, j)
                side_0z = (j,   y_, x_0)
                side_x0 = (x_e, y_, j)
                side_xz = (j,   y_, x_e)

                node_position.append(side_00)
                node_position.append(side_0z)
                node_position.append(side_x0)
                node_position.append(side_xz)

    out_str_ = ""

    for n in node_position:
        line = get_line(n, only_torch)

        out_str_ += "    "
        out_str_ += line
        out_str_ += "\n"

    return out_str_


def main():

    pyramid_height = 5

    header = "5:return {\n"
    body = pyramid(pyramid_height)
    torch_ = pyramid(pyramid_height, True)
    torch = torch_[:-3] + "\n"
    footer = "}"

    out_str = header + body + torch + footer
    print(out_str)

    with open("pyramidtorch_.we", "w") as text_file:
        text_file.write(out_str)


if __name__ == "__main__":
    main()
