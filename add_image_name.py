import os

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
        
        import pandas as pd
        
        df = pd.read_csv("csvs/" + file + ".csv")
        
        df['image'] = files
        
        df.to_csv("csv_copy/" + file + ".csv")
        
        print(file, "done!")