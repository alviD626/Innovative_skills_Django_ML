import time

iteration = 100000000

start = time.time()
list1 = [i+1 for i in range(iteration)]
print(f"duration: {time.time()-start}")


