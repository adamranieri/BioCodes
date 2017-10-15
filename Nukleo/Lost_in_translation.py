from translator import translation
from mutator import mutator
from compare import compare


# very basic interface
print ('Welcome to lost in translation Version Alpha')

# a loop to allow easy reuuse
while(True):
    numb_mut = int(input("please enter the number of nucleotides you wish to mutate"))

    # reads the rna sequnce and creates a new mutated rna sequence
    mutator(numb_mut)

    #returns translations
    pro = list(translation('rnasequence.txt'))
    pro_mut = list(translation('mutated_rna.txt'))

    reader_rna = open ('rnasequence.txt','r')
    rna = list(reader_rna.read())

    reader_rna_mut = open ('mutated_rna.txt','r')
    rna_mut = list(reader_rna_mut.read())

    rna_match = compare(rna,rna_mut)
    pro_match = compare(pro,pro_mut)

    print("matches of rna nucleotides " + str(rna_match))
    print("% of match = " + str((rna_match/len(rna)*100)))
    print("matches of proteins " + str(pro_match))
    print("% of match = " + str((pro_match/len(pro)*100)))

