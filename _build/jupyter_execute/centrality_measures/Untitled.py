#!/usr/bin/env python
# coding: utf-8

# # Eingenvector centrality

# In[1]:


import networkx as nx
import numpy as np
import pandas as pd
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)


# In[2]:


g = nx.read_gml('data/eigenvector_example.gml')
nx.draw(g, with_labels=True)


# In[3]:


A = nx.adjacency_matrix(g)


# In[4]:


val, vec = np.linalg.eig(A.todense())


# In[5]:


nx.degree_centrality(g).


# In[57]:


pd.DataFrame({
    'node': g.nodes, 
    'ev_centrality': np.real(vec[:,0]),
    'degree': nx.degree_centrality(g).values()
})


# In[ ]:




