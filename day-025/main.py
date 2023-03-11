# with open("weather_data.csv", mode="r") as weather_data_file:
#     data = weather_data_file.readlines()
#
#     print(data)


# import csv
#
# with open("weather_data.csv", mode="r") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
print(type(data))
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(sum(temp_list) / len(temp_list))

print(data["temp"].mean())
print(data.temp.mean())
print(data["temp"].max())
print(data.temp.max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
print(data[data.temp == 14])
