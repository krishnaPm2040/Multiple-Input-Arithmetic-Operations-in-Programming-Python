from functools import reduce
import operator
while True:
       try:
              number_of_input=int(input('Enter a number of input:'))
              num=[]
              for count in range(number_of_input):
                     number=float(input(f"Enter a number{count+1}:"))
                     num.append(number)

              
              print("Enter a choose number1/2/3/4",
                            "1.Addition",
                            "2.Subtraction",
                            "3.Multiplication",
                            "4.Division",
                            "5.Squares",
                             sep="\n")
              
              cel=input().strip().lower()
                     
              if cel=="1":
                     add=reduce(operator.add,num)
                     print(f"Total value is:{add}")
                     break

              elif cel=="2":
                     sub=reduce(operator.sub,num)
                     print(f"Total value is:{sub}")
                     break


              elif cel=="3":
                     mul=reduce(operator.mul,num)
                     print(f"Total value is:{mul}")
                     break

              elif cel=="4":
                     div=reduce(operator.truediv,num)
                     print(f"Total value is:{div}")
                     break
        
              
              elif cel=="5":
                    squares=[i**2 for i in num]
                    print(f"Squares of numbers are:{squares}")
                    break
              
              else:
                     print("Enter correct input 1/2/3/4")


       except ZeroDivisionError:
              print("Do not Divied zero")

       except Exception:
              print("Invalied input, please enter number ")

