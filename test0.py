# to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49. If you
# create a program to add these three sets of numbers

def sum(i1,i2):

    result = 0
    for i in range(i1,i2 + 1):
        result +=i
    return result

def main():

    print('sum of int from 1 to 10=',sum(1,10))
    print('sum of int from 20 to 37=',sum(20,37))
main()    


def max(sum1,sum2):

    if sum1 > sum2:
        result = sum1
    else:
        result = sum2
    return result

# invoke the function

z = max(2,1)
print(z)      

def main():
    print(max(1,3))
main()    
    
   
