# mutates the RNA seq and creates a new tct with the mutated seq

from random import *

def mutator(numb_mut):
    nucleotide = open ('rnasequence.txt','r')
    rna = list(nucleotide.read())

    mutationsites = sample(range((len(rna))-1), numb_mut)

    def randomnucleotide():
            chooser = randint(0,3)
            if chooser == 0:
                return 'a'
            if chooser == 1:
                return 'u'
            if chooser == 2:
                return 'c'
            if chooser == 3:
                return 'g'

    for i in range (len(mutationsites)):
        rna[mutationsites[i]] = randomnucleotide()
      
     
    rna = (''.join(rna))
    writer = open ('mutated_rna.txt','w')
    writer.write(rna)
    writer.close()
