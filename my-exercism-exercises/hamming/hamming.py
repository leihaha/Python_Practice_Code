def distance(strand_a, strand_b):
    try:    
        if strand_a == strand_b:
            return 0
        else:
            count = 0
            total = 0
            while count < len(strand_a):
                if strand_a[count] != strand_b[count]:
                    total = total + 1
                count += 1
            return total
    except:
        print("Invalid Input!")

"""
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueErroe("Lengths of strands must be the same.")
    return sum(1 for x, y in zip(strand_a, strand_b) if x != y)
"""