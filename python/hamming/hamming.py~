def distance(seq1, seq2):
    seq1_dict = {spot:base for spot, base in enumerate(seq1)}
    seq2_dict = {spot:base for spot, base in enumerate(seq2)}
    distance = 0
    for spot in seq1_dict:
        if seq1_dict[spot] == seq2_dict[spot]:
            pass
        elif seq1_dict[spot] != seq2_dict[spot]:
            distance += 1
        else:
            return "Sequences are not the same distance."
    return distance      
