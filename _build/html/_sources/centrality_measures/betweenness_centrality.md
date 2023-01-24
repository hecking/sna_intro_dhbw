# Betweenness centrality

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/kite_graph.png
:alt: kite_graph
:width: 300px
```
:::

:::{grid-item-card} Betweenness centrality = Brokarage capacity
A central actor $a$ lies on many shortest paths between 
any other two actors $i$ and $j$.  
If actor $i$ wants to exchange information with another actor $j$, this is only possible by 
having $a$ as a mediator. 

This gives actor $a$ the capacity to broker contacts among 
other actors -- to extract "service charges" and to isolate 
actors or prevent contacts. 
:::
::::

## Definition

Betweenness centrality $c_B(a)$ eines Knotens $a$ der Anteil an kürzesten Pfaden zwischen allen Knotenpaaren $(i, j)$ im Netzwerk 
auf denen $a$ vorkommt.

:::{admonition} Betweenness centrality $c_B(a)$ von Akteur $a$
$c_B(a) = \sum_{i,j \in V_{\backslash a}} \frac{\sigma_{i,j}(a)}{\sigma_{i,j}}$

$\sigma_{i,j}(a)$: Anzahl kürzester Pfade zwischen $i$ und $j$ auf denen $a$ vorkommt.

$\sigma_{i,j}$: Anzahl aller kürzester Pfade zwischen $i$ und $j$.
:::

## Beispiel

```{image} images/betweenness3.png
:alt: betweenness_centrality
:width: 300px
```

**Knoten 3**

```{list-table}
:header-rows: 1

* - $\frac{\sigma_{i,j}(a)}{\sigma_{i,j}}$
  - 1
  - 2
  - 4
  - 5
  - 6
* - **1**
  - 0
  - 0
  - 1
  - 1
  - 1
* - **2**
  - 0
  - 0
  - 1
  - 1
  - 1
* - **4**
  - 1
  - 1
  - 0
  - 0
  - 0
* - **5**
  - 1
  - 1
  - 0
  - 0
  - 0.5
* - **6**
  - 1
  - 1
  - 0
  - 0.5
  - 0
```

$c_B(3) = 6.5$