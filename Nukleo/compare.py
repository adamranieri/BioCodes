#compares two lists to see how often the value at the same index matches

def compare(x,y):
    matches = 0
    for i in range (len(x)):
        if x[i]==y[i]:
            matches = matches +1
    return matches

