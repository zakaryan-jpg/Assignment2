# cons

def profileCreator(tempMatrix):
    length = 0
    profile = dict()
    for key in getDictKeys(tempMatrix):
        profile[key] = []     
    matrix = transposeOfMatrix(tempMatrix)
    for key in profile.keys():
        for dna in matrix:
            profile[key].append(dna.count(key)) 
        length = len(profile[key])
    return profile, length

def consensus(profile, length):
    temp = []
    maximum = 0
    maxVal= ''
    for i in range(length):
        for key, value in profile.items():
            if value[i] > maximum:
                maximum = value[i]
                maxVal = key
        temp.append(maxVal)
        maximum = 0
    return temp

def finalResults(fasta_file):
    inputs = [str(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    matrix = []
    for input in inputs:
        matrix.append(separator(input))
    profile, length = profileCreator(matrix)
    cons = consensus(profile, length)
    consOutput = ''.join(cons)
    profileOutput = ''
    for key, value in profile.items(): 
        strVals = [str(x) for x in value]
        profileOutput += str(key) + ':' + ' ' + (' '.join(strVals)) + '\n'
    finalOutput = consOutput + '\n' + profileOutput
    return finalOutput
    
#helpers
def getDictKeys(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] not in result:
                result.append(matrix[i][j])
    return sorted(result)


def transposeOfMatrix(matrix):
    return [[i[j] for i in matrix] for j in range(len(matrix[0]))]
             
def separator(str):
    result = []
    for character in str: 
        result.append(character)
    return result



fasta_file = "rosalind_cons.txt"
print(finalResults(fasta_file))
