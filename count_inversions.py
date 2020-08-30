#!/usr/bin/env python3

class Counter:

    #other methods give one too many outputs
    def count_inversions(my_list):
        return Counter.merge_sort(my_list)[1]

    def merge_sort(my_list):
        if len(my_list) < 2:
            return my_list,0
        #left is the sorted half, left_count is the number of inversions in that half
        left,left_count = Counter.merge_sort(my_list[:len(my_list)//2])
        right,right_count = Counter.merge_sort(my_list[len(my_list)//2:])
        #both_merged is the sorted array, sun is the sum of all inversions
        both_merged, sun = Counter.merge(left,right)
        return both_merged, sun + left_count + right_count

    #this will return two outputs, the merged array and the counted inversions
    #inputs must be already sorted
    def merge(half1, half2):
        output = [0]*(len(half1) + len(half2))
        i,j,k = 0,0,0
        inversions = 0
        while k < len(output):
            if i == len(half1):
                output[k] = half2[j]
                j+=1
                k+=1
            elif j == len(half2):
                output[k] = half2[i]
                i+=1
                k += 1
            elif half1[i] < half2[j]:
                output[k] = half1[i]
                i+=1
                k+=1
            else:
                output[k] = half2[j]
                j+=1
                k+=1
                inversions += len(half1) - i
        return output, inversions

f = open("many numbers.txt")
unsorted = [0]*100000
pointer = 0
for line in f:
    unsorted[pointer] = int(line)
    pointer += 1
f.close()

print(Counter.count_inversions(unsorted))