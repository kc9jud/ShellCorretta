# pairing.py
# generates matrix elements for a pairing Hamiltonian

def makeOneBodyInts(sp_states):
    oneBodyInts = {}
    for p in range(0, len(sp_states)):
        matel = states[p].n()
        oneBodyInts[(p, p)] = matel
    return oneBodyInts

def makeTwoBodyInts(sp_states):
    twoBodyInts = {}
    for p in range(0, len(sp_states)):
        for q in range(p+1, len(sp_states)):
            for r in range(0, len(sp_states)):
                for s in range(r+1, len(sp_states)):
                    # pairing model
                    if (p+1 == q) and (r+1 == s) and (p % 2 == 0) and (r % 2 == 0):
                        twoBodyInts[((p, q), (r, s))] = -g
    return twoBodyInts
