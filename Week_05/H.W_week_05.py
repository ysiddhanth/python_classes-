# #Part One
# p = int(input("Please Give a Number."))
# if p>0:
#     print("It is a Positive Number.")
# if p<0:
#     print("It is a Negative Number.")
# if p==0:
#     print("It is nor Negative neither Positive Number.")
#
# #Part Two
# n = int(input("Please Give a Number."))
# if (n%2)==0 :
#     print("It is an even number.")
# else:
#     print("It is an Odd Number")
#
#Part Three
# q = int(input("Please give number:"))
# if q < 1:
#         print("Negative prime numbers won't exist.")
# if q == 0:
#      print("0 is neither a prime number or a composite number.")
# if q > 1:
#      for a in range(2,q):
#         if q%a==0:
#             print("It is not a Prime.")
#             break
#         else:
#             print("It is a Prime.")
#
#
#
# #Part Four
#
# interval = int(input("Interval Please:"))
# for num in range(interval + 1):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

# #Part Five
# num = int(input("Number please:"))
# count = 1
# if num<1:
#     print("Factorial for negative integers won't exist.")
# if num==0:
#     print("Factorial is 1.")
# for c in range(1,num+1):
#     count = count*c
#     print(count)
#
#
#
# #part six
# num2 = int(input("Number please:"))
# count = 0
# while count <= num2:
#        count = count + 1
#        if num2 % count == 0:
#         print(count)

#Part Seven
ian = int(input("Please Give number:"))
i = int(input("Please Give 1 digit number:"))
a = int(input("Please Give 2 digit number:"))
n = int(input("Please Give 3 digit number:"))
ian1 = i**3
ian2 = a**3
ian3 = n**3
ian_total = ian1+ian2+ian3
if ian_total==ian:
    print("Yes it is an armstrong number.")
else:
    print("No it is not an armstrong number.")







