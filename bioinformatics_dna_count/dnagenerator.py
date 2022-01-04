import random
nucleotides = ['A','C','G','T']
random_dna = random.choices(nucleotides, k=200)
random_dna_joined = ''.join(random_dna)
print(random_dna_joined)