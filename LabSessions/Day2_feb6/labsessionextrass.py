#python program to sort a list of tuples using lambda
data=[[1,3],[4,6],[8,3],[3.8],[5,0]]
sorted_data=sorted(data,key = lambda x:x[0])
print("sort",sorted_data)

#pyton program to extract year month date n time using lambda
data2={ "Year": 2026,
    "Month": "February",
    "Date": 6,
    "Time": "02:20"}
extracted=list(map(lambda v:v[1], data2.items()))
print(extracted)

#write a python script to concenate the following distionaries to create a new one
new_data={}
data3={ "Year": 2026,
    "Month": "February",
    "Date": 6,
    "Time": "02:20"}
data4={ "Year": 2026,
    "Month": "January",
    "Date": 24,
    "Time": "11.:11"}
data5={ "Year": 2026,
    "Month": "March",
    "Date": 27,
    "Time": "11.:19"}
new_data.update(data3)
new_data.update(data4)
new_data.update(data5)


print("new dict", new_data)