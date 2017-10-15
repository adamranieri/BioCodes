
# this functino translates an rna file into protiens

def translation(file):
    nucleotide = open (file,'r')
    rna = nucleotide.read()
    
   # print(rna)
    
    x = (rna) [::3]
    y = (rna) [1::3]
    z= (rna) [2::3]
    length = len(rna)



    number_of_codons = length/3
    a = list(x)
    b = list(y)
    c = list(z)


    codon = []
#    print (codon)
    for w in range(int(number_of_codons)):
        triplet =  (str(a[w]))+(str(b[w]))+(str(c[w]))         
        codon.append(triplet)
        
    amino = []
    
   # print (codon)
    
    #Codon chart. There is no pattern to why amino acids are coded the way they are
    for x in range (int(number_of_codons)):   

        if codon[x] == 'uuu':
            amino.append('f')
        if codon[x] == 'uuc':
            amino.append('f')
        if codon[x] == 'uua':
            amino.append('l')
        if codon[x] == 'uug':
            amino.append('l')

            
        if codon[x] == 'ucu':
            amino.append('s')
        if codon[x] == 'ucc':
            amino.append('s')
        if codon[x] == 'uca':
            amino.append('s')
        if codon[x] == 'ucg':
            amino.append('s')
        
           
        if codon[x] == 'uau':
            amino.append('y')
        if codon[x] == 'uac':
            amino.append('y')
        if codon[x] == 'uaa':
            amino.append('x')
        if codon[x] == 'uag':
            amino.append('x')

           
        if codon[x] == 'ugu':
            amino.append('c')
        if codon[x] == 'ugc':
            amino.append('c')
        if codon[x] == 'uga':
            amino.append('x')
        if codon[x] == 'ugg':
            amino.append('w')

    ###############################################################################1

        if codon[x] == 'cuu':
            amino.append('l')
        if codon[x] == 'cuc':
            amino.append('l')
        if codon[x] == 'cua':
            amino.append('l')
        if codon[x] == 'cug':
            amino.append('l')

            
        if codon[x] == 'ccu':
            amino.append('p')
        if codon[x] == 'ccc':
            amino.append('p')
        if codon[x] == 'cca':
            amino.append('p')
        if codon[x] == 'ccg':
            amino.append('p')
        
           
        if codon[x] == 'cau':
            amino.append('h')
        if codon[x] == 'cac':
            amino.append('h')
        if codon[x] == 'caa':
            amino.append('q')
        if codon[x] == 'cag':
            amino.append('q')

           
        if codon[x] == 'cgu':
            amino.append('r')
        if codon[x] == 'cgc':
            amino.append('r')
        if codon[x] == 'cga':
            amino.append('r')
        if codon[x] == 'cgg':
            amino.append('r')
            

    #############################################################################2

        if codon[x] == 'auu':
            amino.append('i')
        if codon[x] == 'auc':
            amino.append('i')
        if codon[x] == 'aua':
            amino.append('i')
        if codon[x] == 'aug':
            amino.append('m')

            
        if codon[x] == 'acu':
            amino.append('t')
        if codon[x] == 'acc':
            amino.append('t')
        if codon[x] == 'aca':
            amino.append('t')
        if codon[x] == 'acg':
            amino.append('t')
        
           
        if codon[x] == 'aau':
            amino.append('n')
        if codon[x] == 'aac':
            amino.append('n')
        if codon[x] == 'aaa':
            amino.append('k')
        if codon[x] == 'aag':
            amino.append('k')

           
        if codon[x] == 'agu':
            amino.append('s')
        if codon[x] == 'agc':
            amino.append('s')
        if codon[x] == 'aga':
            amino.append('r')
        if codon[x] == 'agg':
            amino.append('r')
            

    ############################################################################# 3
        if codon[x] == 'guu':
            amino.append('v')
        if codon[x] == 'guc':
            amino.append('v')
        if codon[x] == 'gua':
            amino.append('v')
        if codon[x] == 'gug':
            amino.append('v')

            
        if codon[x] == 'gcu':
            amino.append('a')
        if codon[x] == 'gcc':
            amino.append('a')
        if codon[x] == 'gca':
            amino.append('a')
        if codon[x] == 'gcg':
            amino.append('a')
        
           
        if codon[x] == 'gau':
            amino.append('d')
        if codon[x] == 'gac':
            amino.append('d')
        if codon[x] == 'gaa':
            amino.append('e')
        if codon[x] == 'gag':
            amino.append('e')

           
        if codon[x] == 'ggu':
            amino.append('g')
        if codon[x] == 'ggc':
            amino.append('g')
        if codon[x] == 'gga':
            amino.append('g')
        if codon[x] == 'ggg':
            amino.append('g')

     

    ###################################################################### 4


    return(''.join(amino))
 
  
