def to_rna(dna_str):
    d = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    try:
        return ''.join([d[x] for x in dna_str])
    except KeyError:
        return ''
