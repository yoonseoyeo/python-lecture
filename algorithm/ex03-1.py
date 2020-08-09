def print_pairs(a):

    n = len(a)

    for i in range(0,n-1):
        for j in range(i+1,n):
            print(a[i],"-",a[j])

name=['Tom', 'jerry', 'Mike']

print_pairs(name)

print()
name2=name
name2.append('john')
name2.append('chris')
print_pairs(name2)