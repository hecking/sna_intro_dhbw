#!/usr/bin/env python
# coding: utf-8

# # Übung: Erste Schritte mit NetworkX und Zentralitäten

# **Notwendige Python Pakete**

# In[1]:


#!pip install networkx
#!pip install pandas
#!pip install numpy
#!pip install matplotlib
#!pip install itables


# In[2]:


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)


# ## Zacharies Karate Club
# 
# This is the well-known and much-used Zachary karate club network. The data was collected from the members of a university karate club by Wayne Zachary in 1977. Each node represents a member of the club, and each edge represents a tie between two members of the club. The network is undirected. An often discussed problem using this dataset is to find the two groups of people into which the karate club split after an argument between two teachers. 

# In[3]:


g = nx.karate_club_graph()

nx.draw(g, with_labels=True)


# ## Zentralitäten
# 
# Berechnen Sie Degree, Betweenness, Closeness und Eigenvektor Zentralität.
# 
# - https://networkx.org/documentation/stable/reference/algorithms/centrality.html
# 
# Stellen Sie das Ergebnis als Tabelle da. 

# In[4]:


dc = nx.degree_centrality(g)
bc = nx.betweenness_centrality(g)
cc = nx.closeness_centrality(g)
evc = nx.eigenvector_centrality(g)

pd.DataFrame({
    'degree': dc,
    'closeness': cc,
    'betweenness': bc,
    'eigenvector': evc
})


# ## Netzwerkvisualisierung
# 
# Machen Sie sich mit den Funktionen *draw(G)* und *draw_spring(G)* vertraut.
# 
# - https://networkx.org/documentation/stable/reference/drawing.html
# - https://networkx.org/documentation/stable/auto_examples/drawing/plot_node_colormap.html
# - https://matplotlib.org/stable/tutorials/colors/colormaps.html
# 
# Erstellen Sie eine Abbildung des Netzwerks mit: 
# 
# - Knotengröße korrespondiert mit Degree
# - Betweenness Centrality wird als Farbskala dargestellt. 
# 
# *Tipp: Skalierung des Degrees* 
# 
# > dc = np.array(list(dc.values())) * 200

# In[5]:


nx.draw_spring(g, 
               with_labels=True, 
               node_size=np.array(list(dc.values())) * 200,
               node_color=list(bc.values()),
               cmap=plt.cm.Reds
              )


# ## Twitter Follower Netzwerk von Bundestagsabgeordneten 2019
# 
# https://github.com/WZBSocialScienceCenter/mdb-twitter-network/
# 
# Wer sind die zentralen Personen?

# In[6]:


import networkx as nx
friends = nx.read_gml('mdb_friends.gml')


# Follower Netzwerke sind gerichtete Netzwerke, d.h. es muss zwischen eingehenden und ausgehenden Kanten 
# unterschieden werden. Statt Eigenvector Centrality muss Katz Centrality verwendet werden.

# In[7]:


dc = nx.degree_centrality(friends)
bc = nx.betweenness_centrality(friends)
cc = nx.closeness_centrality(friends)
kc = nx.katz_centrality(friends)

pd.DataFrame({
    'in_degree': dc,
    'closeness': cc,
    'betweenness': bc,
    'katz': kc
})


# In[8]:


friends


# In[ ]:




