import time

iteration = 100000000

start = time.time()
list1 = []
for i in range(iteration):
    list1.append(i + 1)
print(f"duration: {time.time()-start}")


