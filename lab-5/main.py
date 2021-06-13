import fire


def parse_file(s):
    file = open(s, 'r')
    lines = file.readlines()
    m, p = map(int, lines[0].split())
    a = [[0 for x in range(p)] for y in range(m)]
    for line in range(1, len(lines)):
        for i in list(map(int, lines[line].split()))[1:]:
            a[line - 1][i - 1] = 1
    return a


if __name__ == '__main__':
    for i in ['20x20', '24x40', '30x50', '30x90', '37x53']:
        print(fire.get_ans(parse_file('benchmarks/' + i + '.txt')))
