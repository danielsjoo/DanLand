#!/usr/bin/env python3

class Sorter:
    def merge_sort(a):
        if len(a) == 1:
            return a
        return Sorter.merge(Sorter.merge_sort(a[:len(a)//2]),Sorter.merge_sort(a[len(a)//2:]))
    
    def merge(x,y):
        z = [0] * (len(x) + len(y))
        x_pointer = 0
        y_pointer = 0
        z_pointer = 0
        while z_pointer <= len(z) -1:
            if x_pointer == len(x):
                z[z_pointer] = y[y_pointer]
                y_pointer += 1
                z_pointer += 1
                continue
            if y_pointer == len(y):
                z[z_pointer] = x[x_pointer]
                x_pointer += 1
                z_pointer += 1
                continue
            if x[x_pointer]<=y[y_pointer]:
                z[z_pointer] = x[x_pointer]
                x_pointer +=1
            else:
                z[z_pointer] = y[y_pointer]
                y_pointer += 1
            z_pointer += 1
        return z

list1 = [6,5,8,7,3,2,4,1]
print(Sorter.merge_sort(list1))