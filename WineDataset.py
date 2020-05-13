import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def addTwo(myNum):
    return myNum + 2


path = "/home/kuggi/Downloads/winequality-white.csv"

wineData = pd.read_csv(path, sep=";")
# print(wineData.keys(), end=)
# print(wineData.describe())
# np_quality = np.array(wineData["quality"])

wineData.loc[3, "myReview"] = 7
wineData["myReview"] = wineData["quality"].apply(addTwo)
print(wineData.shape)

# high_quality = wineData["quality"] > 8
# myFilter = np.logical_and(wineData["quality"] > 8, wineData["alcohol"] > 12)
# print(myFilter)
# print(wineData[myFilter])

# plt.scatter(wineData["quality"], wineData["sulphates"])
# plt.show()

# print(high_quality)
# print(wineData[high_quality])

# print(np_quality)
# print(np_quality > 6)
# print(np_quality[np.logical_and(np_quality > 4, np_quality < 7)])

# print(wineData.keys())
# print(wineData["quality"])
# print(wineData.describe())
