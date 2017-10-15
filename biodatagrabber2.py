

def datagrabber(file): 
    name = str(file)
    nucleotide = open (name,'r') # put the name of the text file here
    rna = nucleotide.read()

    broken_down = rna.split("\t");
    many = len(broken_down);

    x= 0;
    name = [];
    transcript = [];
    chrom = [];
    strand = [];
    txstart =[];
    txend =[];
    cdstart =[];
    cdsend =[];
    exoncount = [];
    exonstarts = [];
    exonends = [];
    exonframes = [];

    # it works real fast but if you try to actually print any of the lists....
    # your computer will start chugging like a pledge at a fraternity =[

    # so this is the heart of the splicing and dicing
    try:
        for x in range (many) :       
            name.append(broken_down[(x*15)+1 + 15]);
            chrom.append(broken_down[(x*15)+2 + 15]);
            strand.append(broken_down[(x*15)+3 + 15]);
            txstart.append(broken_down[(x*15)+4 + 15]);
            txend.append(broken_down[(x*15)+5 + 15]);
            cdstart.append(broken_down[(x*15)+6 + 15]);
            cdsend.append(broken_down[(x*15)+7 + 15]);
            exoncount.append(broken_down[(x*15)+8 + 15]);
            exonstarts.append(broken_down[(x*15)+9 + 15]);
            exonends.append(broken_down[(x*15)+10 + 15]);
            exonframes.append(broken_down[(x*15)+ 15]);       
    except IndexError:
        pass


    # random mini tests

    exoncount = list(map(int,exoncount));
    cdstart = list(map(int,cdstart));
    cdsend = list(map(int,cdsend));


    return name,chrom,strand,txstart,txend,cdstart,cdsend,exoncount,exonstarts,exonends,exonframes




    #translator = open ('translation.txt','w')
    #translator.write(modification)
    #translator.close()
    
#filename = input()
#a,b,c,d,e,f,g,h,i,j,k = datagrabber(filename)
#print (len(b))
#print (a[2])

