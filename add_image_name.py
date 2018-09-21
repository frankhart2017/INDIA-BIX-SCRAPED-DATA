import os
import pandas as pd

for file in os.listdir("images/"):
    
    if file != ".DS_Store":

        try:
            files = os.listdir("images/" + file + "/cropped")
        except:
            continue
        
        try:
            files.remove(".DS_Store")
        except:
            print("No DS Store")
        
        for i in range(len(files) - 1):
            for j in range(len(files) - i - 1):
                f = files[j].split("image")[1].split(".")[0]
                f = int(f)
                f_1 = files[j+1].split("image")[1].split(".")[0]
                f_1 = int(f_1)
                if (f > f_1):
                    temp = files[j]
                    files[j] = files[j+1]
                    files[j+1] = temp
        
        df = pd.read_csv("csvs/" + file + ".csv")
        
        df['image'] = files
        
        df.to_csv("csv_copy/" + file + ".csv")
        
        print(file, "done!")
        
# Specially for verbal part
        
for file in os.listdir("images_q/"):
    
    if file != ".DS_Store":
        
        try:
            files = os.listdir("images_q/" + file + "/cropped")
        except:
            continue
        
        try:
            files.remove(".DS_Store")
        except:
            print("No DS Store")
            
        num = [int(n.split("image")[1].split(".")[0]) for n in files]
        
        df = pd.read_csv("csv_copy/" + file[:-2] + ".csv")
        
        f = []
        for i in range(df.shape[0]):
            if i in num:
                f.append("image" + str(i) + ".png")
            else:
                f.append("")
        
        df["Question"] = f
        
        if(df.shape[1] == 9):
            df = df.iloc[:, 1:]
        
        df.to_csv("csvs/" + file[:-2] + ".csv")
        
        print(file, "done!")
        
for file in os.listdir("images/"):
    
    if file != ".DS_Store":
        
        try:
            files = os.listdir("images/" + file + "/cropped")
        except:
            continue
        
        try:
            files.remove(".DS_Store")
        except:
            print("No DS Store")
            
        num = [int(n.split("image")[1].split(".")[0]) for n in files]
        
        df = pd.read_csv("csvs/" + file + ".csv")
        
        f = []
        for i in range(df.shape[0]):
            if i in num:
                f.append("image" + str(i) + ".png")
            else:
                f.append("")
        
        df["image"] = f
        
        if(df.shape[1] == 9):
            df = df.iloc[:, 1:]
        
        df.to_csv("csv_copy/" + file + ".csv")
        
        print(file, "done!")
        