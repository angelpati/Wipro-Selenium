import threading

def numbers():
    for i in range(5):
        print("Number",i)
def letter():
    for k in "ABCDE":
        print("Letter",k)
t1= threading.Thread(target=numbers)
t2= threading.Thread(target=letter)
t1.start()
t2.start()
t1.join()
t2.join()