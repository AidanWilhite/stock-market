def evalWork(l):

    # we can average out thier work

    a = 0

    for w in l.Workers:

        # TODO how do we find what values to care about in the weight
        Weight = 1  # print(w.SolCache[5])

        a += (w.sol * Weight)

    a = a/len(l.Workers)

    return a
