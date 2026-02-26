class rotLeft:
    def rotLeft(a,d):
        rotation = d % len(a)
        return a[rotation:] + a[:rotation]
    
#time complexity: O(n)
#space complexity: O(n)

#test cases
print(rotLeft.rotLeft([1, 2, 3, 4, 5], 2)) #[3, 4, 5, 1, 2]
print(rotLeft.rotLeft([1, 2, 3, 4, 5], 4)) #[5, 1, 2, 3, 4]
print(rotLeft.rotLeft([1, 2, 3, 4, 5], 0)) #[1, 2, 3, 4, 5]
print(rotLeft.rotLeft([1, 2, 3, 4, 5], 5)) #[1, 2, 3, 4, 5]