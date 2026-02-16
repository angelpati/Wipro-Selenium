#generators - special type of functions-return one value at a time, on demand

#yield

#memory efficient
#use full large ste of data
#files,retries, batching

#normal function

def numbers():
    return[1,2,3,4]
print(numbers())
#normal function loads all the values in a memory

#generator

def generator():
    print("priting 1")
    yield 1
    print("priting 2")
    yield 2
    print("priting 3")
    yield 3
    print("priting 4")
    yield 4
ret_value=generator()
print(next(ret_value))
print(next(ret_value))
print(next(ret_value))
print(next(ret_value))

#Write a generator to generate numbers from 1 to N
def num_gen(n):
    for i in range(1, n + 1):
        yield i
gen=num_gen(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#Create a generator to generate even numbers only
def even(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i
evengen=even(15)
print(next(evengen))
print(next(evengen))
print(next(evengen))
print(next(evengen))
print(next(evengen))
print(next(evengen))
print(next(evengen))

#Write a generator to read a file line by line









