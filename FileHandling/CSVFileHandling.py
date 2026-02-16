import csv
with open("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//data.csv",'r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//write.csv",'w', newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1, "name", 85])
    writer.writerow([2, "name", 90])
with open("C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//Dataformats//write.csv",'a',newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3,"Angel",100])

