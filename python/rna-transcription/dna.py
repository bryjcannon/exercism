def to_rna(seq):
    bases = {'A':'U', 'C':'G', 'T':'A', 'G':'C'}
    rna_seq =[]
    for base in seq:
        rna_seq.append(bases[base])
    return ''.join(rna_seq)
