import search.two_opt as two_opt
import search.iterated_local as iterated_local
import time


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

    data = {
        'tai20a': read_file('benchmarks/tai20a'),
        'tai40a': read_file('benchmarks/tai40a'),
        'tai60a': read_file('benchmarks/tai60a'),
        'tai80a': read_file('benchmarks/tai80a'),
        'tai100a': read_file('benchmarks/tai100a'),
    }
    for filename in data:
        print(filename)
        results_two_opt = []
        time_executed = 0
        for i in range(100):
            start_time = time.time()
            results_two_opt.append(two_opt.get_ans(*data[filename]))
            time_executed += time.time() - start_time
        print('TWO OPT')
        print(f'TIME: {time_executed/100}')
        best_result = sorted(results_two_opt, key=lambda x: x[1])[0]
        print(f'BEST RESULT: {best_result[1]}')
        print(f'ANSWER: {best_result[0]}')

        file = open(f'answers/two_opt/{filename}.sol', 'w')
        file.write(' '.join(list(map(str, best_result[0]))))


        print()

        results_iterated_local = []
        time_executed = 0
        for i in range(100):
            start_time = time.time()
            results_iterated_local.append(iterated_local.get_ans(*data[filename]))
            time_executed += time.time() - start_time
        print('ITERATED LOCAL')
        print(f'TIME: {time_executed / 100}')
        best_result = sorted(results_iterated_local, key=lambda x: x[1])[0]
        print(f'BEST RESULT: {best_result[1]}')
        print(f'ANSWER: {best_result[0]}')

        file = open(f'answers/iterated_local/{filename}.sol', 'w')
        file.write(' '.join(list(map(str, best_result[0]))))

        print('-----------------------------------------------')


