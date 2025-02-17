def _alternar(arr, ini, fin):
    if fin - ini < 2:
        return arr
    medio = (ini+fin)//2
    arr = _alternar(arr, ini, medio)
    arr = _alternar(arr, medio+1, fin)
    for i in range(1, medio-ini+1, 2):
        arr[ini + i], arr[medio+i] = arr[medio+i], arr[ini + i]
    return arr

def alternar(arr):
    return _alternar(arr, 0, len(arr)-1)

print(alternar(["C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]))