from collections import Counter


def dupl(input):
    input=input.split(' ')
    print(input)
    """for i in range(0,len(input)):
        input[i]="".join(input[i])
    print(input)"""
    unq=Counter(input)  # Counter is used to keep track of occurence of elements in a dictionary. Text as keys and their occurence times as values
    print(unq)
    x=" ".join(unq.keys())
    print(x)


input='Nj is a great man is and so is a Raftaar man and NJ and Raftaar'
dupl(input)