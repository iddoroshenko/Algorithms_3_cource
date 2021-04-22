import search_string.native as native
import search_string.rabin_karp as rabin_karp
import search_string.boyer_moore as boyer_moore
import search_string.knuth_morris_pratt as knuth_morris_pratt
import search_string.aho_corasick as aho_corasick
import time


def test_string_search_algorithm(text, pattern):
    start = time.time()

    print(native.search(text, pattern))
    #print(rabin_karp.search(text, pattern))
    print(boyer_moore.search(text, pattern))
    print(knuth_morris_pratt.search(text, pattern))
    print(aho_corasick.search(text, pattern))

    stop = time.time()
    return stop - start


if __name__ == '__main__':
    print('Hi Anya and Sasha')
    print(native.search("qwerty", "ert"))
    print(rabin_karp.search("qwerty", "ert"))
    print(boyer_moore.search("qwerty", "ert"))
    print(knuth_morris_pratt.search("qwerty", "ert"))
    a = aho_corasick.AhoKorasick()
    a.add_pattern(pattern='acc')
    a.add_pattern(pattern='atc')
    a.add_pattern(pattern='cat')
    a.add_pattern(pattern='gcg')
    a.set_links()
    print(a.search('gcatcg'))

    b = aho_corasick.AhoKorasick()
    b.add_pattern(pattern='a')
    b.add_pattern(pattern='ab')
    b.add_pattern(pattern='bc')
    b.add_pattern(pattern='c')
    b.set_links()
    print(b.search('abacba'))

    f_text = open("benchmarks/bad_t_1.txt", "r")
    f_pattern = open("benchmarks/bad_w_1.txt", "r")
    print(test_string_search_algorithm(f_text.read(), f_pattern.read()))
    f_text = open("benchmarks/bad_t_2.txt", "r")
    f_pattern = open("benchmarks/bad_w_2.txt", "r")
    print(test_string_search_algorithm(f_text.read(), f_pattern.read()))
    f_text = open("benchmarks/bad_t_3.txt", "r")
    f_pattern = open("benchmarks/bad_w_3.txt", "r")
    print(test_string_search_algorithm(f_text.read(), f_pattern.read()))
    f_text = open("benchmarks/bad_t_4.txt", "r")
    f_pattern = open("benchmarks/bad_w_4.txt", "r")
    print(test_string_search_algorithm(f_text.read(), f_pattern.read()))
