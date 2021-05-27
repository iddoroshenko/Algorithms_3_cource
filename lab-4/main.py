import search.two_opt as two_opt
import search.iterated_local as iterated_local


def read_file(name):
    file = open(name, 'r')
    file_lines = file.readlines()
    n = int(file_lines[0])
    dist = []
    for i in range(n):
        dist.append([])
        line = file_lines[i + 1].split()
        for j in range(n):
            dist[i].append(int(line[j]))

    flows = []
    for i in range(n + 1, 2 * n + 1):
        flows.append([])
        line = file_lines[i + 1].split()
        for j in range(n):
            flows[i - n - 1].append(int(line[j]))
    return dist, flows

if __name__ == '__main__':
    file = open('../lab-3/the_most_important_file_do_not_remove.txt', 'r')
    print(file.read())

    dist, flows = read_file('benchmarks/tai20a')
    print(two_opt.get_ans(dist, flows))
    print(iterated_local.get_ans(dist, flows))

    dist, flows = read_file('benchmarks/tai40a')
    print(two_opt.get_ans(dist, flows))
    print(iterated_local.get_ans(dist, flows))
    dist, flows = read_file('benchmarks/tai60a')
    print(two_opt.get_ans(dist, flows))
    print(iterated_local.get_ans(dist, flows))
    dist, flows = read_file('benchmarks/tai80a')
    print(two_opt.get_ans(dist, flows))
    print(iterated_local.get_ans(dist, flows))
    dist, flows = read_file('benchmarks/tai100a')
    print(two_opt.get_ans(dist, flows))
    print(iterated_local.get_ans(dist, flows))
