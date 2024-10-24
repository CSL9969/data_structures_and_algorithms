def merge_sort(array, a=0, b=None):

    if b == None:
        b = len(array)
    
    if a < b-1:
        m = (a + b) // 2
        merge_sort(array, a, m)
        merge_sort(array, m, b)

        left = array[a:m]
        right = array[m:b]

        i, j = 0,0
        pointer = a

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[pointer] = left[i]
                i += 1

            else:
                array[pointer] = right[j]
                j += 1
            
            pointer += 1

        while i < len(left):
            array[pointer] = left[i]
            i += 1
            pointer += 1

        while j < len(right):
            array[pointer] = right[j]
            j += 1
            pointer += 1

array = [1,0,13,35,2,53,52,2,13,6,14,7,45]
merge_sort(array)
print(array)