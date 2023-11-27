def pal(x, y):
    pal2=[('G', 'C'), ('C', 'G'), ('A','T'), ('T','A')]
    for i in range (len(x)-y+1):
        z=x[i:i+y]
        if all(((z[j], z[y-j-1])) in pal2 for j in range(y)):
            print(i+1,y)

dna='ATATCGGCAGCTTTGGAATCACGCAACCCCTACCGCTCGACAAAGCGATTTAAGGTTACAGTCTTATATTAGGACACGGGGACCTTACGGGATAGTGCCACCTGCTAGTCGAAATAACCCAACGTACGTAAGTATCCTGTCCGTCGTGCATTTTGATTAAGTTAGACTCCTCAGATTTAATAGAGGAACTCGGTAGGCAGCCTAATTTTACCGCCTCCGGGACGCAGTTTTCGTTGTAGCTAGCGTCAAGCTCCGTGCGATCTCCACCCATGAGTGGTATGGTAGAGGAGACTGGTGATGCTACAGCAAAGATGAAAAACGATTCCTGAGGAGTACTGTTTGTGTAATTTTCATTAACATTGGGCGTGACCCAAACCCTTGCCTGCCACAGTCGTTATCTTTTCGGCGGGCCCAAAACTTCGTTATAAAGGATCACAATCTGGGCATATAAGCAGTACCGTGTCATGACACCTTACAAATCCACTGGATTAGATTCTAGTAAATCCCGCGATGACTCTTACCGAACCATGGTTTTCGGTTCCGTTGCAGCCTGGATAGCATGGTCCTGTCCGTACGTCCGCACGAAGGCACCTTCTCGCAAGACAGATCTCCAAAGAAGGCTGTCCTTTGTACTCCCAGGGCTGCGCCACATTCTACTCTGGACCTTATAGGCAAATTGACACCGTCATACGACATTGGGGGGTCCACACCAGTAGAGACATGCGGCCAACTGGTAACAGTGTAGCAATTTTATTTTCGATGCATTACAGAAACTCACCTTTGCAGTACAGCGGAGTTGGTTACAGGGTTATCCTAGATCCAGCTGTGGTGGACAGCCGGTATCACACAGAGTGCGTTCCGTACGACGCCTCAACCAGGGGTCTACTTTGCGTCGGTTGAACTAGGGGAAGTAACTAACACTACTAGCGC'
for i in range(4,14,2):
    pal(dna, i)