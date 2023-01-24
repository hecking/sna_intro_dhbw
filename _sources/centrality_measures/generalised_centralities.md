---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Generalisierte Zentralitätsmaße - Eigenvector centrality & Co.

## Einführendes Beispiel

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/eigenvector_example.png
:alt: ev_example
:width: 300px
```
:::

:::{grid-item-card} Welcher Knoten ist wichtiger $a$ oder $b$?
- Beide haben eine hohe Betweenness Centrality
- $b$ hat einen höheren Degree
- $a$ hat eine höhere Closeness Centrality
:::
::::

:::{admonition} Generelle Idee
:class: tip, dropdown
Ein Knoten ist so wichtig wie seine Nachbarn!
:::

## Eigenvector Centrality

**Idee:** Ein Knoten ist so wichtig wie seine Nachbarn, die so wichtig sind wie ihre Nachbarn, die so wichtig sind wie ihre Nachbarn, ...

:::{admonition} Eigenvector centrality $x_a$ von Akteur $a$
$x_a = \sum_{i \in N(a)} x_i = \sum_{i \in V} A_{a,i} x_i$

$N(a)$: Nachbarn von $a$

$A$: Adjazenzmatrix
:::

:::{admonition} Ausgedrückt als Matrixmultipliation
$A \vec{x} = \lambda \vec{x}$

Die Lösung ist Äquivalent für das Lösen des [Eingenwertproblems](https://de.wikipedia.org/wiki/Eigenwertproblem) für die Adjazenzmatrix $A$. 
Hierzu gibt es Standartverfahren in der linearen Algebra.

$\vec{x}$: Eigenvektor von $A$

$\lambda$: Eigenwert von $A$
:::

### Berechnung der Eigenvektor Centrality

```{code-cell} ipython3
import numpy as np
import networkx as nx
import pandas as pd
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)

g = nx.read_gml('data/eigenvector_example.gml')
nx.draw(g, with_labels=True)
```

**Berechnung der Eigenvektoren der Adjazenzmatrix $A$**

```{code-cell} ipython3
A = nx.adjacency_matrix(g)
val, vec = np.linalg.eig(A.todense())

print(vec)
```

:::{admonition} Eine $n \times n$ hat $n$ Eigenwerte und Eigenvektoren. Welcher soll genommen werden?
:class: dropdown
**Den Vektor zum größten Eigenwert!**
Eine reelle quadratische Matrix mit nur positiven oder 0 Einträgen hat einen eindeutigen größten Eigenwert. Dessen korrespondierender Eigenvektor enthält nur strikt positive Einträge.
[Perron–Frobenius theorem](https://de.wikipedia.org/wiki/Satz_von_Perron-Frobenius) 
:::

```{code-cell} ipython3
pd.DataFrame({
    'node': g.nodes, 
    'ev_centrality': np.real(vec[:,0]),
    'degree': nx.degree_centrality(g).values()
})
```

## Katz centrality (Alpha centrality)

Generalisierung der Eigenvektorzentralität auf gerichtete Netzwerke. 

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/katz_example.png
:alt: ev_example
:width: 300px
```
:::

:::{grid-item-card} Ein Knoten ist so wichtig wie seine Nachbarn.
- **Problem:** Was ist mit Knoten, die keine Nachbarn haben?
- **Lösung:** Jeder Knoten erhält von Beginn an ein kleines Gewicht, typtischerweise $1$
:::
::::

:::{admonition} Katz centrality $c_{Katz}(a)$ von Akteur $a$
$c_{Katz} = \sum_k^\infty \sum_{j \in V} \alpha^k (A^k)_{a,i}$

Gewichtete Anzahl der Pfade von Knoten $a$ zu allen anderen Knoten.

$\alpha \in (0, 1]$: Gewichtungsfaktor. Längere Pfade zählen weniger. 

$A$: Adjazenzmatrix
:::

:::{admonition} Matrixschreibweise
$\vec{x}  = ((I - \alpha A)^{-1} - I) \vec{I}$

$I$: Einheitsmatrix 

$\vec{I}$: Einsvector (zur Bildung der Zeilensummen der Matrix $((I - \alpha A)^{-1} - I)$)
:::

## Page Rank

Entwickelt zum Ranking von Suchmaschinenenresultaten.

**Idee:** Eine Webseite ist wichtig, wenn viele wichtige Webseiten auf sie verlinken. 

:::{admonition} Random Surfer Modell
Ein fiktiver User surft zufällig durch das Web indem Links auf Webseiten verfolgt werden. Einige Seiten werden dabei häufiger erreicht als andere (wie bei Katz Centrality). 

Unterschied zu Katz Centrality: Der Random Surfer verfolgt Links nur mit einer Wahrscheinlichkeit $d$. Mit Wahrscheinlichkeit $1 - d$ springt er zufällig zu einer x-beliebigen Seite (Gibt URL direkt im Browser ein).  

$c_{PR}(a) = \frac{1-d}{|V|} + d \sum_{i \in N_{in}(a)}\frac{c_{PR}(i)}{od_i}$

$N_{in}(a)$: Eingehende Nachbarn. (Auf $a$ verlinkende Seiten)

$od_i$: Out-degree von Knoten $i$. (Anzahl der Links auf der Seite)
:::