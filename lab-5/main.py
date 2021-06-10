
import fire


if __name__ == '__main__':
    file = open('benchmarks/20x20.txt', 'r')
    lines = file.readlines()
    m, p = map(int, lines[0].split())
    a = [[0 for x in range(p)] for y in range(m)]
    for line in range(1, len(lines)):
        for i in list(map(int, lines[line].split()))[1:]:
            a[line-1][i-1] = 1
    for i in range(1000):
        print(fire.get_ans(a))
