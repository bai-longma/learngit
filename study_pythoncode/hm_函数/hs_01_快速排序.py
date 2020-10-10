def qsort(L):
    if len(L) <= 1:
        return L
    small = qsort([lt for lt in L[1:] if lt < L[0]])
    hall = qsort([lt for lt in L[1:] if lt >= L[0]])
    return small + L[0:1] + hall

List = [1,56,48,12,95,32,8,1,3,8,6,52,12]
print(qsort(List))