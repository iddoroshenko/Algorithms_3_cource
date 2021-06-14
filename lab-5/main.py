import fire
import time


def parse_file(s):
    file = open(s, 'r')
    lines = file.readlines()
    m, p = map(int, lines[0].split())
    a = [[0 for x in range(p)] for y in range(m)]
    for line in range(1, len(lines)):
        for i in list(map(int, lines[line].split()))[1:]:
            a[line - 1][i - 1] = 1
    return a


def get_line_from_lists(lst):
    line = ''
    for l in lst:
        line += '[' + ' '.join(list(map(str, l))) + ']'
    return line


if __name__ == '__main__':
    for i in ['20x20', '24x40', '30x50', '30x90', '37x53']:
        total_time = 0
        answers = []
        file = open('answers/' + i + '.sol', 'w')
        for j in range(10):
            start = time.time()
            answers.append(fire.get_ans(parse_file('benchmarks/' + i + '.txt')))
            total_time += time.time() - start
        print(f'FILE: {i} - TIME: {total_time/10}')
        answers = sorted(answers, key=lambda x: x[0], reverse=True)
        file.write(get_line_from_lists(answers[0][1]) + '\n')
        file.write(get_line_from_lists(answers[0][2]))

