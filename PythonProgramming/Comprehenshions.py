#create lits using a single line of code instaed of loops
#syntax
# square of the number
square=[x**2 for x in range(1,6)]
print(square)

#with condition
cond=[x for x in range(10) if x%2==0]
print(cond)

#data comprehenshion increased by 10
dict={"A":2000, "B": 3000,"C": 4000}
updated_dict={k:v +1.0*v for k,v in dict.items()}
print(updated_dict)

#filtering of dictionary
employess={"Angel":"Active","Abhi":"Active","Anmol":"Inactive"}
active_employees={k:v for k,v in employess.items() if v=="Active"}
print(active_employees)
