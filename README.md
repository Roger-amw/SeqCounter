# SeqCounter
Script to count occurences of first n nucleotides in reads in FASTQ files

Usage:

SeqCounter [-h] -r1 READ1 -r2 READ2 [-n NUMBER] [-p | --percentage | --no-percentage] [--top TOP] [--r1out R1OUT] [--r2out R2OUT]

Examples:

Print help.
```
$ python SeqCounter.py -h

usage: SeqCounter [-h] -r1 READ1 -r2 READ2 [-n NUMBER] [-p | --percentage | --no-percentage] [--top TOP] [--r1out R1OUT] [--r2out R2OUT]

Script to count occurences of first n nucleotides in reads in FASTQ files

options:
  -h, --help            show this help message and exit
  -r1 READ1, --read1 READ1
                        FASTQ file with R1 reads
  -r2 READ2, --read2 READ2
                        FASTQ file with R2 reads
  -n NUMBER, --number NUMBER
                        Number of first n nucleotides to count (default: 10)
  -p, --percentage, --no-percentage
                        Output results as percentage of total reads also (default: False) (default: False)
  --top TOP             Output top-n results (default: 10)
  --r1out R1OUT         Output R1 results csv file name (default: R1_counts.csv)
  --r2out R2OUT         Output R2 results csv file name (default: R2_counts.csv)
  
  ```
  Output top 5 counts for the first 6 nucleotides.
  ```
  $ python SeqCounter.py -r1 test/R1.fastq -r2 test/R2.fastq -p --r1out ABCD.csv -r2out EFGH.csv -n 6 --top 5
  ```
