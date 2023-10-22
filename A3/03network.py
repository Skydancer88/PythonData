import pandas as pd
import networkx as nx
import shutil
import wget
import os

from bokeh.io import output_notebook, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx

output_notebook()

# get data file if does not exist
if os.path.isfile('lesmis.mtx') == False:
    filename = wget.download('http://nrvis.com/download/data/misc/lesmis.zip')
    shutil.unpack_archive('lesmis.zip')

G = nx.Graph()
with open('lesmis.mtx') as in_file:
  lines = in_file.readlines()[2:]
  for line in lines:
    n1, n2, w = line.split()
    if n1 not in G.nodes():
      G.add_node(n1)
    if n2 not in G.nodes():
      G.add_node(n2)
    G.add_edge(n1, n2, weight=int(w))
print(G)

#Choose a title!
title = 'Les Miserables character network'

#Establish which categories will appear when hovering over each node
HOVER_TOOLTIPS = [("Character", "@index")]

#Create a plot — set dimensions, toolbar, and title
plot = figure(tooltips = HOVER_TOOLTIPS, tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom', x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), title=title)

#Create a network graph object with spring layout
# https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html
network_graph = from_networkx(G, nx.spring_layout, scale=10, center=(0, 0))
#Set node size and color
network_graph.node_renderer.glyph = Circle(size=15, fill_color='skyblue')

#Set edge opacity and width
network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

#Add network graph to the plot
plot.renderers.append(network_graph)

#Show the plot
show(plot)
