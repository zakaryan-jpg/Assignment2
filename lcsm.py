# lcsm

from Bio import SeqIO

def lcsm(dna_strings):
    shortest_seq = min(dna_strings, key=len)
    length = len(shortest_seq)

    for i in range(length, 0, -1):
        for j in range(length - i + 1):
            subs = shortest_seq[j:j+i]
            in_all = True
            for dna in dna_strings:
                if subs not in dna:
                    in_all = False
                    break
            if in_all:
                return subs


fasta_file = "rosalind_lcsm 2.txt"
dna_strings = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
print(lcsm(dna_strings))
