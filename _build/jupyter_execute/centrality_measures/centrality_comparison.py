#!/usr/bin/env python
# coding: utf-8

# # Vergleich von Zentralitätsmaßen

# In[1]:


import networkx as nx
import pandas as pd
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)


# ## Beispiel Kite-Graph
# 
# > Krackhardt, David. “Assessing the Political Landscape: Structure, Cognition, and Power in Organizations”. Administrative Science Quarterly. 35 (2): 342–369. doi:10.2307/2393394. JSTOR 2393394. June 1990.

# In[2]:


kg = nx.krackhardt_kite_graph()
label_mapping = {0: 'Andre', 1: 'Beverly', 2: 'Carol', 3: 'Diane', 4: 'Ed', 5: 'Fernando', 6: 'Garth', 7: 'Heather', 8: 'Ike', 9: 'Jane'}
kg = nx.relabel_nodes(kg, label_mapping)

nx.draw(kg, with_labels=True)


# In[3]:


pd.DataFrame({
    'degree': nx.degree_centrality(kg),
    'closeness': nx.closeness_centrality(kg),
    'betweenness': nx.betweenness_centrality(kg)
})


# ## Beispiel Game of Thrones Netzwerk
# 
# Knoten des Netzwerks sind Charaktären in der Buchreihe "A Song of Ice and Fire" von George R. R. Martin. 
# Zwei Knoten sind miteinander verbunden wenn deren Namen mit höchstens 15 Wörtern Abstand genannt wurden.
# 
# Quelle: https://github.com/mathbeveridge/asoiaf

# In[4]:


edges = pd.read_csv('data/asoiaf-all-edges.csv')
g = nx.from_pandas_edgelist(edges, 'Source', 'Target', edge_attr=True)


# In[5]:


pd.DataFrame({
    'degree': nx.degree_centrality(g),
    'closeness': nx.closeness_centrality(g),
    'betweenness': nx.betweenness_centrality(g)
})


# In[ ]:




