#!/usr/bin/env python
# coding: utf-8

# # Arten von Netzwerken

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt


# ## Zufallsgraphen (Erdös-Renyi Netzwerke)

# In einem Erdös-Renyi Netzwerk mit $n$ Knoten werden je zwei Knoten mit einer Wahrscheinlichkeit $p$ miteinander verbunden. Dementsprechend ist der durchschnittliche Degree der Knoten:
# 
# $\hat{d} = p (n - 1)$

# In[2]:


g1 = nx.erdos_renyi_graph(100, 0.1)


# In[3]:


hist1 = nx.degree_histogram(g1)
plt.plot(hist1, "b-", marker="o")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.show()


# # Skalenfreie Netzwerke
# 
# ![ba_graph](images/barabasi.png)

# Skalenfreie Netzwerke tauchen überall auf. Diese lassen sich nicht durch eine Skala (Typischer Degree) charakterisieren.

# In[4]:


g2 = nx.scale_free_graph(100)

hist2 = nx.degree_histogram(g2)
plt.plot(hist2, "b-", marker="o")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.show()


# **Die Wahrscheinlichkeit von extremen Fällen, d.h. Knoten mit sehr hohem Degree (Hubs) ist in skalenfreien Netzwerken sehr viel höher**
# 
# Die Degree-Verteilung folgt einem inversen Potenzgesetz:
# 
# $P(d=k) \sim k^{-\gamma}$
# 
# Skalenfreie Netzwerke sind sehr robust gegenüber Knotenausfällen.
# 
# 

# **Preferential Attachment**
# 
# The rich get richer.
# 
# - Knoten kommen nacheinander in das Netzwerk und verbinden sich mit $x$ existierenden Knoten.
# - Die Warscheinlichkeit sich mit einem Knoten zu verbinden erhöht sich, wenn dieser bereits viele Verbindungen hat.
# 
# ![pa](images/preferential_attachment.png)

# **Beispiele:**
# 
# - WWW
# - Co-Autoren Netzwerke
# - Instagram
# - Facebook
# - ...

# In[ ]:




