name = input("Enter your name??\n")
if (name == "Rabin Dhami"):
    print("YOu are passed")
else:
<<<<<<< HEAD
    print("helloooo")
=======
    print("First Day")
>>>>>>> 2a101f6d0df8f82a72c04a29b066d6b9af82b339
class sum:
    def __init__(self,x,y):
        self.x = x
        self.y= y
        
    def display(self):
        sum = self.x+ self.y;
        print("sum is ",sum)
        
s = sum(2,3)

s.display()

class Fib:
    def __init__(self,n):
        self.n = n
    def calc(self):
        a,b=0,1
        print(a)
        for i in range(self.n-1):
           a = b
           b = a+b
           print(a)
           
f = Fib(20)
f.calc()
<<<<<<< HEAD
a = int(input("Enter the no"))
b= int(input("eNTER yhe no"))
sum=a+b
print(sum)
=======
import random
#Guessing the random number using binary search with least attempts
def binary_search(target):
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        mid = (low + high) // 2
        attempts += 1
        
        if mid == target:
            return attempts
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  
# Generate a random target number between 1 and 100
target_number = random.randint(1, 100)
print("Target Number:", target_number)

# Perform binary search
attempts = binary_search(target_number)
print("Number of attempts:", attempts)

>>>>>>> 2a101f6d0df8f82a72c04a29b066d6b9af82b339
