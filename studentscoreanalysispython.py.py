import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv("Expanded_data_with_more_features.csv")

# Check the column names to ensure correctness
print(df.columns)

# Resetting the index of the DataFrame
df = df.reset_index(drop=True)

# Printing the head of the DataFrame after resetting the index
print(df.head())
# Convert the column to string type
df['yStudWkly'] = df['yStudWkly'].astype(str)

# Now you can use the .str.replace() method
df['yStudWkly'] = df['yStudWkly'].str.replace("05-Oct", "5-10")

# Corrected count plot function name
plt.figure(figsize=(5, 15))
ax = sns.countplot(data=df, x="Gender")
ax.bar_label(ax.containers[0])
plt.title("gender distribution")
plt.show() 

gb = df.groupby("ParentEduc").agg({"MathScore" : 'mean',"ReadingScore" : 'mean',"WritingScore" : 'mean'})
print(gb) 

sns.heatmap(gb)
plt.title("relationship between parents education and students score")
plt.show() 


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore" : 'mean',"ReadingScore" : 'mean',"WritingScore" : 'mean'})
print(gb1) 

plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot = True)
plt.show() 

sns.boxplot(data = df , x = "MathScore")
plt.show()


sns.boxplot(data = df , x = "ReadingScore")
plt.show()


print(df["EthnicGroup"].unique())

#distribution of ethnic group 
groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["groupA" , "groupB" , "groupC" , "groupD" , "groupE"]
mlist = [groupA["EthnicGroup"] , groupB["EthnicGroup"] ,  groupC["EthnicGroup"]  , groupD["EthnicGroup"] , groupE["EthnicGroup"]]
plt.pie(mlist , labels = l , autopct = "%1.2f%%")
plt.title("Distribution of ethnic group ")
plt.show()

ax = sns.countplot(data = df , x = 'EthnicGroup')
ax.bar_label(ax.containers[0])