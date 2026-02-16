import json
from json import JSONDecodeError

with open("C:/Users/ANGEL PATI/PycharmProjects/PythonAdvanceProgramming/Dataformats/employee.json",'r') as file:
    data=json.load(file)
print(data)
print(data["name"])

with open("C:/Users/ANGEL PATI/PycharmProjects/PythonAdvanceProgramming/Dataformats/nested.json",'r')as file:
    data=json.load(file)
print(data["user"]["profile"]["email"])


# writing in the json by using dump
data={
  "name": "Angel",
  "role": "Student",
  "experience": 5,
  "skills": ["Python", "Automation", "API","Java"]

}

with open("C:/Users/ANGEL PATI/PycharmProjects/PythonAdvanceProgramming/Dataformats/writing.json",'w')as file:
    json.dump(data,file)

#update
#read the json file
#modify the data
#write it back
with open("C:/Users/ANGEL PATI/PycharmProjects/PythonAdvanceProgramming/Dataformats/update.json",'r')as file:
    data=json.load(file)
data["experience"]=6
with open("C:/Users/ANGEL PATI/PycharmProjects/PythonAdvanceProgramming/Dataformats/update.json",'w')as file:
    json.dump(data,file, indent= 4)


import json


##try:
   ## with open(" C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//ExceptionHandling.py",'r')as file:
        ##data=json.load(file)
        #print(data)
#except FileNotFoundError:
   # print("Error:File not found, please mention a valid file")

file_path=" C://Users//ANGEL PATI//PycharmProjects//PythonAdvanceProgramming//PythonProgramming//ExceptionHadling.py"
with open(file_path,'r')as file:
    content=file.read()
    print(content)
except FileNotFoundError:
    raise FileNotFoundError(f"Error: The file '{file_path}' was not found. Please provide a valid file.")




