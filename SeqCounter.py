#! python

import sys
import os
import argparse
import pandas as pd
from Bio import SeqIO

parser=argparse.ArgumentParser(
    prog='SeqCounter',
    description='''Script to count occurences of first n nucleotides in reads in FASTQ files ''',
    epilog='''Author: Anna Wąsowska, 2023''')
parser.add_argument('-r1', '--read1', type=str, required=True, help='FASTQ file with R1 reads')
parser.add_argument('-r2', '--read2', type=str, required=True, help='FASTQ file with R2 reads')

parser.add_argument('-n', '--number', type=int, default=10, help='Number of first n nucleotides to count (default: 10)')
parser.add_argument('-p', '--percentage', action=argparse.BooleanOptionalAction, default=False, help='Output results as percentage of total reads also (default: False)')
parser.add_argument('--top', type=int, default=10, help='Output top-n results (default: 10)')
parser.add_argument('--r1out', type=str, default="R1counts.csv", help='Output R1 results csv file name (default: R1_counts.csv)')
parser.add_argument('--r2out', type=str, default="R2counts.csv", help='Output R2 results csv file name (default: R2_counts.csv)')
args=parser.parse_args()

fq_file_R1 = SeqIO.parse(open(args.read1), "fastq")
fq_file_R2 = SeqIO.parse(open(args.read2), "fastq")

out_fileR1 = os.path.realpath(args.read1).rsplit("/",1)[0] + "/" + args.r1out
out_fileR2 = os.path.realpath(args.read2).rsplit("/",1)[0] + "/" + args.r2out

def df_transpose_and_count_percent(file):
    seqDict = dict()
    for key in file:
        if (str(key.seq[0:args.number]) in seqDict):
            seqDict[str(key.seq[0:args.number])] += 1
        else:
            seqDict[str(key.seq[0:args.number])] = 1
    seqDictSorted = dict(sorted(seqDict.items(), key=lambda x:x[1], reverse=True))
    df = pd.DataFrame({'Sequence': list(seqDictSorted.keys()), 'Counts': list(seqDictSorted.values())})
    df['Percent'] = round(df.Counts / df.Counts.sum() *100, ndigits=3)
    return df

if (args.percentage == True):
    df_transpose_and_count_percent(fq_file_R1).loc[0:(args.top-1)].to_csv(out_fileR1, index=False, header=True)
    df_transpose_and_count_percent(fq_file_R2).loc[0:(args.top-1)].to_csv(out_fileR2, index=False, header=True)
else:
    df_transpose_and_count_percent(fq_file_R1).loc[0:(args.top-1)].to_csv(out_fileR1, columns=['Sequence', 'Counts'], index=False, header=True)
    df_transpose_and_count_percent(fq_file_R2).loc[0:(args.top-1)].to_csv(out_fileR2, columns=['Sequence', 'Counts'], index=False, header=True)
