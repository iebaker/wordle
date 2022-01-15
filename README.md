# wordle
### Corpus Generation
`python cleaner.py <word length> <input file> <output file>`  
Input file contains one string per line of arbitrary length. Output file will be one string per line containing strings from input file 
cast to lowercase, only including those which have the correct length and no special characters. 

### Solver
`python solver.py <corpus file> <target word>`  
Runs solver given a corpus as generated above, and a target word from that corpus. Behavior is undefined if target word is not contained in
corpus file. Output is a sequence of guesses terminating in the correct guess.

Requires python 3.8+
