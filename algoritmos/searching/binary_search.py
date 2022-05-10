def binary(arr, x):
    min = 0
    alt = len(arr) - 1
    medi = 0
 
    while min <= alt:
 
        medi = (alt + min) // 2
 
        if arr[medi] < x:
            min = medi + 1
 
        elif arr[medi] > x:
            alt = medi - 1
 
        else:
            return medi
 
    return -1
