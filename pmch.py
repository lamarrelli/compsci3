import math

def calculate_perfect_matchings(rna_string):
    a_count = rna_string.count('A')
    u_count = rna_string.count('U')
    c_count = rna_string.count('C')
    g_count = rna_string.count('G')

    total_matchings = math.factorial(min(a_count, u_count)) * math.factorial(min(c_count, g_count))

    return total_matchings

def main():
    rna = "GCAUGGUUGAGACUAAGAGUUUUUUGAUUAACCCAGUGUCUCCCACGCGGACUAAAAACUAGCACCCGCAGGGUUCUG"
    result = calculate_perfect_matchings(rna)
    print(result)

if __name__ == "__main__":
    main()

