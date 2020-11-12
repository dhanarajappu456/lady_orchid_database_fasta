#This is orchid databse extracted from NCBI

from  Bio import SeqIO
for record in SeqIO.parse('ls_orchid.fasta','fasta'):
    print(record.id)
    print(repr(record.seq))
    print(len(record))
    
    
    

    


