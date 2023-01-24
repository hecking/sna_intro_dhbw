#!/usr/bin/env python
# coding: utf-8

# # Clique Percolation Beispiel
# 
# **Americal College Football Netzwerk (Girvan and M. E. J. Newman, Proc. Natl. Acad. Sci. USA 99, 7821-7826 (2002).).**
# 
# http://www-personal.umich.edu/~mejn/netdata/

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import k_clique_communities

g = nx.read_gml('data/football.gml')


# **Struktur des Netzwerks**
# 
# College Teams sind miteinander verbunden, wenn sie gegeneinander gespielt haben. Da die amerikanische College Liga in Divisionen organisiert ist, finden die meisten Spiele innerhalb der eigenen Division statt. Dadurch entsteht ein Netzwerk mit Community Struktur.

# In[2]:


nx.draw_spring(
    g, node_color=list(nx.get_node_attributes(g, 'value').values()), 
    cmap=plt.cm.Dark2, 
    with_labels=True,
    font_size=8
)


# In[3]:


communities = k_clique_communities(g, k=4)


# In[4]:


list(communities)


# In[ ]:




