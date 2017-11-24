def to_rna(dna_strand):
    strand = {'G': 'C', 'C': 'G', 'T': 'A', 'A':'U'}
    try:
        return "".join([strand[item] for item in dna_strand])
    except KeyError:
        raise ValueError(" This is a Invalid input!")

to_rna('XXX')