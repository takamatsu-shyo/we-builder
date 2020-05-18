import re

def content_len(_input):
    print(_input)
    print("Length: ", len(_input))


def level_shifter(_list, _unit):

    shifted_list = []

    for l in _list:
        y_elem = re.findall("y\"] = .", l)
        print(y_elem)
        print(type(y_elem))
        _y = int(y_elem[0][-1:])
        print(_y)

        shift = 6 * _unit
        _y_shifted = _y + shift
        print(_y_shifted)

        shifted_y_elem = y_elem[0][:-1] + str(_y_shifted)
        print(shifted_y_elem)

        shifted_l = re.sub("y\"] = .", shifted_y_elem, l)
        print(shifted_l)

        shifted_list.append(shifted_l)

    return shifted_list
        

# Read a file
with open("double_spiral.we") as f:
    one_line = f.readlines()

print(type(one_line))
print(len(one_line))


# Insert nextline
lines_ =  re.sub("},", "},\n", str(one_line))
# Nextline for header and footer
lines_head = re.sub("{{", "{\n{", lines_)
lines = re.sub("}}", "}\n}", lines_head)

print(type(lines))
print(lines.count("\n"))


# Split to modules
lines_torch = re.findall('.*torch.*', lines)
content_len(lines_torch)
lines_gold = re.findall('.*gold.*', lines)
content_len(lines_gold)
lines_cobble = re.findall('.*cobble.*', lines)
content_len(lines_cobble)

lines_spiral = lines_torch + lines_gold + lines_cobble


lines_obsidian = re.findall('.*obsidian.*', lines)
content_len(lines_obsidian)


# How many unit do you need?
unit_num = 100

# Main spirals
main_lines = []

for i in range(unit_num):
    l = level_shifter(lines_spiral, i)
    main_lines += l
    main_lines += ","

content_len(main_lines)

# Top one
top_lines = level_shifter(lines_obsidian, unit_num - 1)
print(top_lines)


# Make a string to write
header = "5:return {\n"
footer = "}\n"
body_str = ""

for l in main_lines:
    body_str += str(l)
    body_str += "\n"

#body_str += ",\n"

for l in top_lines:
    body_str += str(l)
    body_str += "\n"



writing_str = header + body_str[:-2] + footer

print(writing_str)

f = open("double_spiral_.we", "w+")
f.write(writing_str)
