from operator import length_hint
import time

test = [1,2,3]
test.append([4,5,6])
test.extend([4,5,6])
print(test)

a = time.process_time()
print(len(test))
b = time.process_time()
print(length_hint(test))
c = time.process_time()

print("1번:{:.30f}, 2번:{:.30f}".format(a,b))
d = b-a
e = c-b
print("1번:{:.30f}, 2번:{:.30f}".format(d,e))