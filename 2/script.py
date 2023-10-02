list1 =['one','two','three']
list1.append('four')
del list1[-1]
if 'ten' not in list1:
    print ('ten is not in list1')
list1.sort()
list1.remove('three')
print (list1.reverse())
print (list1.count('ONE'))
print (len(list1))
list1[0]='1'
list1[0]= int(list1[0])
print (list1)