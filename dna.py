import sys

class Compress():
    def __init__(self, genome: str):
        self._bit_string = 0
        self._compress(genome)
        

    def _compress(self, genome: str):
        for nuc in genome:
            self._bit_string <<= 2

            if nuc == 'A':
                self._bit_string |= 0b00
            elif nuc == 'T':
                self._bit_string |= 0b01
            elif nuc == 'G':
                self._bit_string |= 0b10
            elif nuc == 'C':
                self._bit_string |= 0b11
            else:
                print('Chozahax: {} ???'.format(nuc))
            
       # print(self._bit_string)


    def decomp(self):
        #print('>>> ', self._bit_string)

        decomp_string = ''
        for _ in range(0, self._bit_string.bit_length() - 1, 2):
            print('>>> ', self._bit_string)
            pair_bit_str = self._bit_string & 0b11
            print(pair_bit_str)
            if pair_bit_str == 0b00:
                decomp_string += 'A'
            elif pair_bit_str == 0b01:
                decomp_string += 'T'
            elif pair_bit_str == 0b10:
                decomp_string += 'G'
            elif pair_bit_str == 0b11:
                decomp_string += 'C'
            else:
                print('Chozahui: {} ???'.format(decomp_string))
            self._bit_string >>= 2
         
        print(decomp_string[::-1])
            



genome_string = 'GCCGCATGTACGTCGTAGCTACGTAGCTAGCTACGTGTJAGCTAGTCGATGTACGTACGTACGCTGCTAGCATGCTAGCTAGCTAAC'*1000
genana = Compress( genome_string )
print(sys.getsizeof(genome_string))
print(sys.getsizeof(genana._bit_string))
print(len(genome_string))
