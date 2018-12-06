from fixed_point import fixbv

a = fixbv(min=-100, max=100, res=2**-8)
print(a)
b=fixbv(format=a.format)
print(b)






