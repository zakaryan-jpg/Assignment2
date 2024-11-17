# splc

from Bio import SeqIO


def cutout(fullStr, toCut):
    if toCut in fullStr:
        fullStr = fullStr.replace(toCut, '')
    return fullStr

def transcription(fullStr):
    fullStr = fullStr.replace('T', 'U')
    return fullStr


def prot(rna, codon_table):
    protein = ""

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon_table[codon] == "Stop":
            break
        protein += codon_table[codon]

    return protein

def finalOutput(fasta_file):
    codon_table = {
            "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
            "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
            "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
            "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
            "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
            "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
            "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }

    
    inputs = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    fullstr = inputs[0] 
    tocut = []
    for i in range(1, len(inputs)):
        tocut.append(inputs[i])
    for cut in tocut:
        fullstr = cutout(fullstr, cut)
    fullstr = transcription(fullstr)
    return prot(fullstr, codon_table)


fasta_file = "rosalind_splc 2.txt"
print(finalOutput(fasta_file))
