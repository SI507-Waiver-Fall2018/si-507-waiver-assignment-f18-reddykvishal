# Imports -- you may add others but do not need to
import plotly as pt
import csv
pt.tools.set_credentials_file(username="kvishalr", api_key="KNDjitatUVdRKwvVpZVY")
# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
nounlist=[]
nouncount=[]
csvfile = open("noun_data.csv", "r")

reader = csv.reader(csvfile)
count = 0
for line in reader:
    if count > 0:
        nounlist.append(line[0])
        nouncount.append(line[1])
    count+=1

graphytask = pt.graph_objs.Bar(x=nounlist, y=nouncount,
    marker=dict(
        color=['rgba(0,255,255,1)', 'rgba(255,0,255,1)',
               'rgba(255,255,0,1)', 'rgba(0,0,0,0.5)',
               'rgba(69,16,116,1)']))
data = [graphytask]
layout = pt.graph_objs.Layout(title='Nouns data', width=800, height=640)
fig = pt.graph_objs.Figure(data=data, layout=layout)

pt.pt.image.save_as(fig, filename='part4_viz_image.png')
