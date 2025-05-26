import random 

from timeit import default_timer as timer 

import matplotlib.pyplot as plt 

def partition(array, low, high): 

 pivot = array[high] 

 i = low - 1 

 for j in range(low, high): 

 if array[j] <= pivot: 

 i = i + 1 

 (array[i], array[j]) = (array[j], array[i]) 

 (array[i + 1], array[high]) = (array[high], array[i + 1]) 

 return i + 1 

def quickSort(array, low, high): 

 if low < high: 

 pi = partition(array, low, high) 

 quickSort(array, low, pi - 1) 

 quickSort(array, pi + 1, high) 

x=[] 

y=[] 

for i in range(3): 

 # Generate a list of random integers 

 n=int(input("\nenter the value of n:")) 

 x.append(n) 

 arr = [random.randint(0, 1000) for _ in range(n)] 

 print("\nthe array elements are",arr) 

 start_time = timer() 

 ind=quickSort(arr,low=0,high=n-1) 

 end_time = timer() 

 print("array elements are ", arr) 

 elapsed_time = end_time - start_time 

 y.append(elapsed_time) 

 print("time taken=", elapsed_time) 
# Plot the results 

plt.plot(x,y) 

plt.title('Time Taken for quick sort') 

plt.xlabel('n') 

plt.ylabel('Time (seconds)') 

plt.show()
