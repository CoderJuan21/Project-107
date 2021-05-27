import csv
import pandas as pd
import statistics
import plotly.express as px

df = pd.read_csv("Reaaallldata.csv")

mean = df.groupby(["student_id", "level"], as_index= False)["attempt"].mean()

fig=px.scatter(mean, x = "student_id", y = "level", size = "attempt", color = "attempt")
fig.show()