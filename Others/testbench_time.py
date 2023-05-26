from time_class import Time

t1 = Time(seconds=60)
t2 = Time(minutes=60)
t3 = Time(hours=10)

print(t1)
print(t2)
print(t3)

print(t1+t2)
print(t2+t3)
print(t1+t3)

print(t3-t2)
print(t2-t1)
print(t3-t1)

