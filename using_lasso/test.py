a = list(range(1,11))
a.reverse()
print(a)

for r2_threshold,r22_threshold in zip(a,list(range(1,10))):
    print( float(r2_threshold) / 10, float(r22_threshold) / 10)

