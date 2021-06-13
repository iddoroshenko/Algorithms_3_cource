import math
import random
import numpy as np


def S(i, j, a):
    both_counter = 0
    only_i_counter = 0
    only_j_counter = 0
    for x in range(len(a)):
        if a[x][i] == 1 and a[x][j] == 1:
            both_counter += 1
        elif a[x][i] == 1:
            only_i_counter += 1
        elif a[x][j] == 1:
            only_j_counter += 1

    return both_counter / (both_counter + only_j_counter + only_i_counter)


def fitness(cells_machines, cells_details, a, num_of_cells):
    n_1 = 0
    n_0_in = 0
    n_1_out = 0
    for x in a:
        for y in x:
            n_1_out += y
    for i in range(num_of_cells):
        for machines in cells_machines[i]:
            for detail in cells_details[i]:
                n_1 += a[machines][detail]
                if a[machines][detail] == 0:
                    n_0_in += 1
    n_1_out -= n_1
    if (n_1 + n_0_in) == 0:
        return
    return (n_1 - n_1_out) / (n_1 + n_0_in)


def single_move(current_solve, a, num_of_cells):
    n = len(a[0])  # число деталей
    cells_details = current_solve[1].copy()
    best_f = -9999
    best_cells_details = []
    best_cells_machine = []
    detail_to_move = random.randint(0, n - 1)
    old_cell = 0
    for i in range(len(cells_details)):
        if detail_to_move in cells_details[i]:
            old_cell = i
            cells_details[old_cell].remove(detail_to_move)
            break
    for i in range(len(cells_details)):
        if i != old_cell:
            cells_details[i].append(detail_to_move)
            new_cells_machine = machines_cells_selecting(a, cells_details, num_of_cells)
            new_f = fitness(new_cells_machine, cells_details, a, num_of_cells)
            if new_f > best_f:
                best_cells_machine = new_cells_machine.copy()
                best_cells_details = cells_details.copy()
                best_f = new_f
            cells_details[i].remove(detail_to_move)
    cells_details[old_cell].append(detail_to_move)
    return best_f, best_cells_details, best_cells_machine


def exchange_move(current_solve, a, num_of_cells):
    n = len(a[0])  # число деталей
    cells_details = current_solve[1].copy()
    best_f = -9999
    best_cells_details = []
    best_cells_machine = []
    detail_to_move = random.randint(0, n - 1)
    old_cell = 0
    for i in range(len(cells_details)):
        if detail_to_move in cells_details[i]:
            old_cell = i
            cells_details[old_cell].remove(detail_to_move)
            break
    for i in range(len(cells_details)):
        if i != old_cell and len(cells_details[i]) != 0:
            detail_to_move2 = cells_details[i][random.randint(0, len(cells_details[i]) - 1)]
            cells_details[i].append(detail_to_move)
            cells_details[i].remove(detail_to_move2)
            cells_details[old_cell].append(detail_to_move2)
            new_cells_machine = machines_cells_selecting(a, cells_details, num_of_cells)
            new_f = fitness(new_cells_machine, cells_details, a, num_of_cells)
            if new_f > best_f:
                best_cells_machine = new_cells_machine.copy()
                best_cells_details = cells_details.copy()
                best_f = new_f
            cells_details[i].remove(detail_to_move)
            cells_details[i].append(detail_to_move2)
            cells_details[old_cell].remove(detail_to_move2)
    cells_details[old_cell].append(detail_to_move)
    return best_f, best_cells_details, best_cells_machine


def machines_cells_selecting(a, cells_details, num_of_cells):
    m = len(a)  # число станков
    cells_machines = [[] for x in range(num_of_cells)]
    for machine in range(m):
        error = [0 for x in range(num_of_cells)]
        for cell in range(num_of_cells):
            for detail in cells_details[cell]:
                if a[machine][detail] == 0:
                    error[cell] += 1
                else:
                    for i in range(num_of_cells):
                        if i != cell:
                            #for detail2 in cells_details[cell]:
                                #if a[machine][detail2] == 1:
                            error[i] += 1

        ans = np.argmin(error)
        cells_machines[ans].append(machine)

    return cells_machines


def get_ans(a):
    num_of_cells = 2

    n = len(a[0])  # число деталей
    m = len(a)  # число станков
    b = [[0 for x in range(n)] for y in range(n)]

    similarity = []

    for i in range(n):
        for j in range(i + 1, n):
            b[i][j] = S(i, j, a)
            if b[i][j] != 0:
                similarity.append((b[i][j], i, j))
    similarity.sort(reverse=True)
    best_solve = [-9, [], []]

    goto_1 = True
    while True:
        if goto_1:
            #delta = similarity[int(math.sqrt(len(similarity)))][0]
            #delta = [1/(x+2) for x in range(num_of_cells - 1)]
            delta = [similarity[(x+1)*int(math.sqrt(len(similarity)))][0] for x in range(num_of_cells - 1)]
            cells_details = [[] for x in range(num_of_cells)]
            cells_details[0].append(similarity[0][1])
            cells_details[0].append(similarity[0][2])
            delta_counter = 0
            for i in range(1, len(similarity)):
                if similarity[i][0] > delta[delta_counter]:
                    if similarity[i][1] not in cells_details[delta_counter]:
                        cells_details[delta_counter].append(similarity[i][1])
                    if similarity[i][2] not in cells_details[delta_counter]:
                        cells_details[delta_counter].append(similarity[i][2])
                else:
                    delta_counter += 1
                if delta_counter == num_of_cells - 1:
                    break
            for detail in range(n):
                f = True
                for i in range(num_of_cells-1):
                    if detail in cells_details[i]:
                        f = False
                if f:
                    cells_details[num_of_cells - 1].append(detail)
            cells_machines = machines_cells_selecting(a, cells_details, num_of_cells)

            current_best_solve = (fitness(cells_machines, cells_details, a, num_of_cells), cells_details, cells_machines)  # S**
            if current_best_solve[0] > best_solve[0]:
                best_solve = current_best_solve  # S*
            current_solve = current_best_solve  # S
            T_0 = 1
            T_f = 0.2
            T = T_0
            alpha = 0.5
            L = 1000
            D = 10
            counter = 0
            counter_mc = 0
            counter_trapped = 0
            counter_stagnant = 0

        goto_1 = False
        while counter_mc < L and counter_trapped < L / 2:
            new_solve = single_move(current_solve, a, num_of_cells)  # S_c
            if counter % D == 0:
                new_solve = exchange_move(current_solve, a, num_of_cells)
            if new_solve[0] > current_best_solve[0]:
                current_best_solve = new_solve
                counter_stagnant = 0
                counter_mc += 1
                current_solve = new_solve
                continue
            if new_solve[0] == current_best_solve[0]:
                current_solve = new_solve
                counter_stagnant += 1
                counter_mc += 1
                continue
            delta = new_solve[0] - current_solve[0]
            if math.e ** (delta / T) > random.uniform(0, 1):
                current_solve = new_solve
                counter_trapped = 0
            else:
                counter_trapped += 1
            counter_mc += 1
        if T <= T_f or counter_stagnant > 100:
            if current_best_solve[0] > best_solve[0]:
                best_solve = current_best_solve
                num_of_cells += 1
                goto_1 = True
            else:
                break
        else:
            T = T * alpha
            counter_mc = 0
            counter += 1
            continue
    return best_solve