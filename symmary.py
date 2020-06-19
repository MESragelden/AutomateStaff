# ctrl+k+c for comment 
# ctrl+k+u for uncomment
import  random,sys,os,cv,math
# math 
print("5/2 = ",5/2) # 2.5 regular division    
print("5//2 = ",5//2) # 2 integer division
print("5%2 = ",5%2) # 1 Reminder
print("5 ** 2 = ",5 ** 2) # 25 5 to the power 2 --> pow(5,2) 

# quotes and output  
i = "I "
l = "Like "
u = "You"
m = "i \"ve got a mail" # use \ to ignore " or use multiple quotes '''  wewew''"AD""Ad" """"

print("%s %s %1.8f "% (i,l,math.pi))

# Lists
L1 = [3.1,3.5,2,5.5,8,5,5]
L2 = [7,8,9,10,15,6]
merge = L1+L2 # merge them into one new list
combine = [L1,L2] # list with pointer to every list m, change in any one affect this list
L3 = L2[2:] # new pointer to same L2 , if want to copy content # L3 = L2+[]
L4 = L2.copy()  # copy list to new one
print(merge," ",combine)
L2.remove(6) 
L1.remove(8)
print(merge," ",combine)
print(L3)
print(L4[1:])
L3.insert(0,53.250) # insert at index = 0  value = 53.250 
L2.pop() # remove last element
# Check if element in a list 
print("3 in L3",3 in L3)
print("3 not in L3",3 not in L3)
print ("number of occucrence ",L1.count(5))
# tuple 
print('*' * 20,"Tuple",'*' * 20)
t = (1,23,4,5,6,8)
t2 = (1,2,22)
t3 = t+t2
print(min(t3),max(t3),len(t3))
print(t3)
print ("3 in t3",3 in t3)
print ("3 not in t3",3 not in t3)
print ("number of occucrence ",t3.count(5))
print('*' * 20,"Dictionary {Key : Value}",'*' * 20)

# key may be num - str - list - tuple
point_values = {
    (0,0):8,
    (1,0):6,
    (2,0):4,
    (0,1):10,
    (0,2):-3
}
print (point_values[(0,0)])
print ((0,0) in point_values)
del point_values[(0,2)]
print(point_values)
point_values[(0,0)] = -90
print(point_values)
print(point_values.get((0,0)))
print(point_values.keys(),point_values.values())
print((list(point_values.values())))
print((type(point_values.values())))
for k,v in point_values.items():
    print (k,"*"*8,v)
for i in [-8,0,9,8,11,11,88]:
    print (i)
print ("*"*20,"Modules","*"*20)
print(random.randint(0,999))

#name =sys.stdin.readline()
#print("Hellllo ",name)
print ("*"*20," Strings ","*"*20)
s = "it's ok "
print("it's ok "[::-1])
print(s.isalpha())