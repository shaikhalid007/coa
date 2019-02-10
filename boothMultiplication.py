#written by Rick sanchez
#wabalaba dub dub
from bitstring import BitArray


def max(p, q):
    if(p>q):
        return p
    return q


def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val-2**bits
    return val


def combine(A,bQ,l):
    ans = []
    for i in range(l):
        ans.append(int(A[i]))
    for i in range(l):
        ans.append(int(bQ[i]))
    finalans = ''.join(str(e) for e in ans)
    if (ans[0]==1):
        finalans=twos_comp(int(finalans, 2), len(finalans))
    print(finalans)


def arith_shift_right(x, amt):
    l = x.len
    x = BitArray(int = (x.int >> amt), length = l)
    return x


def booth(m, mc, q, x, y):
    l=max(x, y)
    bQ = BitArray(int=q, length=l)
    bM = BitArray(int=m, length=l)
    A = BitArray(int=0, length=l)
    qm1 = 0
    for i in range(l):
        temp = []
        if bQ[l-1] > qm1:
            A = BitArray(int=A.int + mc, length=l)
        elif bQ[l-1] < qm1:
            A = BitArray(int=A.int + bM.int, length=l)
        temp.append(A[0])
        temp.append(A[l-1])
        qm1=bQ[l-1]
        A = arith_shift_right(A, 1)
        A[0]=temp[0]
        bQ = arith_shift_right(bQ, 1)
        bQ[0]=temp[1]
        print(A, end=' ')
        print(bQ, end=' ')
        print(int(qm1))
    combine(A,bQ,l)


booth(-52, 52, 59, 7, 7)
