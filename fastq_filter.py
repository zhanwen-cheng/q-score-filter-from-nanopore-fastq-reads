#! /usr/bin/env python3
######################################
######by Cheng Zhanwen 20201023#######
###a python script to filter bases ###
#####lower than the given q_value ####
######################################

#import time
#start = time.time()
import getopt
import sys
from Bio import SeqIO

opts, args = getopt.getopt(sys.argv[1:],'-h-f:-q:',['help','file=','q_value='])
for opt_name, opt_value in opts:
    if opt_name in ('-h','--help'):
        print("fastq_filter.py -f <file name> -q <min q_value>")
        print("fastq_filter.py --file=<file_name> -q_value=<min_q_value>")
        sys.exit()
    if opt_name in ('-f','--file'):
        file_name = opt_value
    if opt_name in ('-q','q_value'):
        q_value = opt_value

for seq_record in SeqIO.parse(file_name,"fastq"):
    #print(seq_record.seq)
    print(">"+seq_record.id)
    new_seq_list=[]
    for i in range(0,len(seq_record)):
        if seq_record.letter_annotations["phred_quality"][i]< int(q_value):
            new_seq_list.append('N')
        else:
            new_seq_list.append(seq_record.seq[i])
        #print(seq_record.seq[i], i, seq_record.letter_annotations["phred_quality"][i], new)
    new_seq="".join(new_seq_list)
    print(new_seq)
    #for i in range(0,len(seq_record)):
        #print(seq_record.seq[i], i, seq_record.letter_annotations["phred_quality"][i], new_seq[i])
#end = time.time()
#print(end-start)      
