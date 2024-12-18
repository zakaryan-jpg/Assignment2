# mrna

codon_count = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2
}

MOD = 1000000
stop_cod_count = 3

def mrna(protein):
    rna_num = [0] * (len(protein) + 1)
    rna_num[0] = 1
    
    for i in range(1, len(protein) + 1):
        rna_num[i] = rna_num[i-1] * codon_count[protein[i-1]] % MOD
    
    return (rna_num[len(protein)] * stop_cod_count) % MOD

protein = "MCDASKCNQCEHHGPKKQLFATPDEYAWMMSMYRWIQCWQGIEMWWMDLVNPRLKWATGAVGFLKHMENPKPHPKPHSHMIWTLQWTAGRGLTGMERGDQSKLDDSTTEYLANNVYCQAGKPLSPYAHRKCCSEERGGKDQGRGRVKHKLYLDKQENMYYHYYCGTGRFMYKKHIYTEPTNEEEKPPWSFLRMPDRISSDMHILTKDNYSEQWQKVQIVCCGIWAHSITVYLGKQKTNNKEGFETKELKFSSYTSDCTDACIVTWQVEFNKTTDQWDSCGFMACIEFLSRKREIMYWPGVNRFHFERNNFCGLEVFSILAVPLKQDNAMGMTDIAHFEDHMNAYILSPADDWQEFFIIEMPIFFTLDLERIWKFTTMIVCVWNYHHMERGWIMLTENAGHCSGGESYWAFNDFEGHIYWYETYMNQGRCPFMWLRQIMTWDFTPINRPEGMCASSCFNDQKKYPFVACPRPAMDWTLIGSICTYVTAYQYCSKAMVPVSQERVLMPKTHKQFFAPIRQCQCPCGSTIVKIDLVQTALRDNLKNYCSNVLSDRVWNRFMIWPCENIFWRADTVRDVRARTAWRDITPKTESTLTDAWQKQLVLQHRKSSRRMAQCQCQIINYHVHYWHCSQDQHHFYEFPSCRHHMRNLTWCIVALAWWINETKHPMYRDYSAEKIMNCFWHLKVSASMRFKVCAIKQGMHNMIGIMLCFGNQQCKKMWWVCVDIYRIVLFWPIDHKCKKTWMACQGTNAHLWDIRFYWAEGDTKGYCYFACGYYFKGKETQEFTHHYFALAKPVGALELQCCTMHYSKVHVMWIHLIQRCFLHYTCQTGTHQRYHHENQHNEGTIYQQPMNVIFWFFSKMWLTSNFPPSPTELFWTYLESKCYIRWRLGPSLKPWYSIFGVGSKQFEGCCWHISLLYTQSCTDAYTNCIDKPMLTSHTRWGPSGTWTGHPLLNANRDKRQSCGKRELAEGPICPICHLDCWMYDNYGLSNYWHTTAT"
print(mrna(protein))
