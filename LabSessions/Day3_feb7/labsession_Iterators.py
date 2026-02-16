#Create a custom iterator that prints numbers from 1 to 5
def num():
    for i in range(1,5):
        yield i
itera = num()
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))





#Write an iterator class that returns next even number

class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers  # store the list
        self.index = 0          # start from index 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration

nums = [1, 3, 4, 5, 6, 7, 7, 8, 9, 40]

even_iter = EvenIterator(nums)

print(next(even_iter))  # 4
print(next(even_iter))  # 6
print(next(even_iter))  # 8
print(next(even_iter))  # 40


#Write a generator to generate numbers from 1 to N
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

def read_file(file_name):

    with open(file_name, 'r') as file:
        content = file.read()
        print(f"{file_name} Reading")
red=read_file(file1.text,file2.txt)
print(next(red))
print(next(red))

#Create a generator for Fibonacci series.





#Write a generator that simulates retry attempts (max 3 tries)







