import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [len(data[data["Primary Fur Color"] == "Gray"]),
              len(data[data["Primary Fur Color"] == "Cinnamon"]),
              len(data[data["Primary Fur Color"] == "Black"])]
}

dataFrame = pandas.DataFrame(data_dict)

dataFrame.to_csv("summary.csv")
