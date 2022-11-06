import pandas as pd
import os

path = r'D:\= ='

# data = pd.read_csv(path + os.sep + "task1.csv")

for i in range(1,11):
    os.mkdir(path + os.sep + "helloWorld" + str(i))

for i in range(1, 11):
    if(i%2==0):
        for j in range(1,i+1):
            f = open(path + os.sep + "helloWorld" + str(i) + os.sep + "helloWorld" + str(j) + ".txt", "w")
            f.write("helloWorld" + str(j) + ".txt")
f.close()
