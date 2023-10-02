# testing timeit()
import timeit
 
# code snippet to be executed only once
mysetup = "5+5-65+3453"
 
print(timeit.timeit(mysetup))