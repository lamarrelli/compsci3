import math

def gc_content_probability(dna_string, gc_content):
    gc_prob = gc_content / 2
    at_prob = (1 - gc_content) / 2

    log_probability = 0
    for base in dna_string:
        if base in 'GC':
            log_probability += math.log10(gc_prob)
        elif base in 'AT':
            log_probability += math.log10(at_prob)

    return log_probability

def log_probability_array(dna_string, gc_contents):
    result = [gc_content_probability(dna_string, gc) for gc in gc_contents]
    return result

dna_string = "ACTACCCAGGATCTACGTGGGCAGTGTGCGGGAGTTGGGCGCACAGAAAATAGAACGTCGACAATGTCGGAAACAAGCCCCCG"
gc_contents = [0.067, 0.135, 0.223, 0.287, 0.371, 0.395, 0.451, 0.543, 0.582, 0.641, 0.733, 0.762, 0.824, 0.908]

result = log_probability_array(dna_string, gc_contents)
for value in result:
    print(value, end=' ')
