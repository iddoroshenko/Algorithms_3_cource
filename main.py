import search_string.native as native
import search_string.rabin_karp as rabin_karp
import search_string.boyer_moore as boyer_moore
import search_string.knuth_morris_pratt as knuth_morris_pratt

if __name__ == '__main__':
    print('Hi Anya and Sasha')
    print(native.search("qwerty", "ert"))
    print(rabin_karp.search("qwerty", "ert"))
    print(boyer_moore.search("qwerty", "ert"))
    print(knuth_morris_pratt.search("qwerty", "ert"))
