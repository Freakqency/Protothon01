  
import math  
def rmsValue(arr, n): 
    square = 0
    mean = 0.0
    root = 0.0
      
    for i in range(0,n): 
        square += (arr[i]**2) 
      
    mean = (square / (float)(n)) 
      
    root = math.sqrt(mean) 
      
    return root 
  
if __name__=='__main__': 
    val=input("please enter a some values")
    arr = val.split(",")
    arr=list(map(int,arr))
    n = len(arr) 
    print(rmsValue(arr, n)) 
