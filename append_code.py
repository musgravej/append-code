import random
import string


class Global:
    def __init__(self):
        self.code_set = set()
        self.letters = {index: letter for index, letter in enumerate(string.ascii_uppercase, start=1)} 


def return_code(drop, g):
    """
    returns a 7 character random code, starting with a drop code
    but not in g.code_set
    """
    drop_codes = {1: 'C', 2: 'R', 3: 'T', 4: 'S'}
    code = ""
    while code not in g.code_set:
        build_code = drop_codes[drop]
        while len(build_code) < 7:
            # Use a number
            if bool(random.randint(0, 1)):
                build_code += str(random.randint(0, 9))
            # Use a letter
            else:
                build_code += g.letters[(random.randint(1, 26))]

        code = build_code
        g.code_set.add(code)

    return code


def write_rec(g):
    f = open('33404 trilix main list after ncoa.txt', 'r').readlines()
    header = f[0]
    for drop in range(1, 5):
        with open('33404_Trilix_Drop {}.txt'.format(drop), 'w', newline='') as s:
            s.write("drop\tcode\t{}".format(header))
            for line in range(1, len(f)):
                s.write("{}\t{}\t{}".format(drop, return_code(drop, g), f[line]))


if __name__ == '__main__':
    g = Global()
    write_rec(g)
