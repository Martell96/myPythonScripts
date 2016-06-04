#! /usr/bin/env python3

def PascalTriangle(n):
    triangle = []
    for row in range(n):
        triangle.append([])
        if row == 0:        
            for column in range(n):
                triangle[row].append(1)
        else:
            for column in range(n-row):
                if column == 0:
                    triangle[row].append(1)
                else:
                    triangle[row].append(triangle[row-1][column]+triangle[row][column-1])
    return triangle

for row in PascalTriangle(10):
    print (row)
