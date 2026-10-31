import pandas as pd
import matplotlib.pyplot as plt

# 1
df = pd.read_csv("bicycle_data.csv")

# 2
# Columns:
#   - Date: timestamp of each hourly count (e.g. "10/02/2012 01:00:00 PM").
#           Read in as a string; should be datetime.
#   - Total: total bicycles crossing the Fremont Bridge sidewalks in that hour.
#   - West: bicycles on the west sidewalk in that hour.
#   - East: bicycles on the east sidewalk in that hour.
#   The counts are read as float64 because of missing values; they should be
#   integers, so convert them to pandas' nullable integer type Int64.
df.columns = ["Date", "Total", "West", "East"]
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")
df[["Total", "West", "East"]] = df[["Total", "West", "East"]].astype("Int64")

# 3
df["EW_Total"] = df["East"] + df["West"]
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

# 4
df_2016 = df[df["Year"] == 2016].copy()

# 5
# Missing data: 1 time point (2016-03-13 02:00, start of daylight saving time).
df_2016 = df_2016.dropna(subset=["West", "East"])

# 6
counts_by_hour = df_2016.groupby("Hour")["EW_Total"].sum()
counts_by_hour.plot(kind="bar")
plt.title("Fremont Bridge Bicycle Counts by Hour of Day (2016)")
plt.xlabel("Hour of Day")
plt.ylabel("Total Bicycle Count")
plt.tight_layout()
plt.savefig("counts_by_hour.png")

# 7
# Busiest hour: 17 (5-6 PM).
mean_by_hour = df_2016.groupby("Hour")["EW_Total"].mean()
busiest_hour = mean_by_hour.idxmax()
print("Busiest hour:", busiest_hour)