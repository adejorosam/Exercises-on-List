'''Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.
(g) Print how many integers in the list are less than 5.'''
L=[]
for i in range(1,21):
    L.append(i)
print(L)
print(len(L))
print(L[-1])
print(L[::-1])
count=0
for item in L:
    if 5 in L:
        count+=1
        print(count)
        print('Yes')
        break
else:
    print('No')
print(L[::19])
del L[::19]
print(L)
L.sort()
count=0
for item in L:
    if 5 in L:
        if item < 5:
            count+=1
print(count)

