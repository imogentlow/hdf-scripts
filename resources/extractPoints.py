import pandas as pd

# target
# lon 176.322, lat -37.82
lat_ind = 47
lon_ind = 121

dirArr = []
fileArr = []

dirF = open("./granules.txt", "r")
fileF = open("./dataset.txt", "r")

for li in fileF:
    fileArr.append(li.strip())

for li in dirF:
    dirArr.append(li.strip())


for file in fileArr:
    df = pd.DataFrame()
    for di in dirArr:
        read_path = "../csv/rebuilt/" + di + "/" + file + ".csv"
        granule_df = pd.read_csv(read_path, header=None)
        point = granule_df.iloc[lat_ind, lon_ind]
        df = df.append({"T": di, "sample": point}, ignore_index=True)
    print(file, "\n", df, "\n\n")
    write_path = "../csv/prepro/" + file + ".csv"
    df.to_csv(write_path)