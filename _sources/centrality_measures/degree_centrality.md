# Degree centrality

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/kite_graph.png
:alt: kite_graph
:width: 300px
```
:::

:::{grid-item-card} Degree centrality = Local importance
Opportunities and alternatives to immediate influence others, 
acquire and spread information. 

Actors who have more ties 
have greater opportunities because they have more choices. 
This autonomy makes them less dependent on any specific 
other actor, and hence more powerful.
:::
::::

## Definition

Degree centrality $c_D(a) eines Knotens $a$ ist die Anzahl der Nachbarn im Netzwerk.

:::{admonition} Degree centrality $c_D(a)$ von Akteur $a$
$c_D(a) = \mathbf{A} \times \mathbf{1}$, d.h. Zeilensummen der Adjazenzmatrix $\mathbf{A}$

$\mathbf{I}$: Einsvektor
:::

In gerichteten Netzwerken:

:::{admonition} Outdegree centrality $c_{OD}(a)$ von Akteur $a$
$c_{OD}(a) = \mathbf{A} \times \mathbf{1}$, d.h. Zeilensummen der Adjazenzmatrix $\mathbf{A}$
:::

:::{admonition} Indegree centrality $c_{ID}(a)$ von Akteur $a$
$c_{ID}(a) = \mathbf{A^T} \times \mathbf{1}$, , d.h. Spaltensummen der Adjazenzmatrix $\mathbf{A}$
:::

## Beispiel

```{image} images/kite_graph.png
:alt: kite_graph
:width: 300px
```

```{list-table}
:header-rows: 1

* - $a$
  - $c_D(a)$
* - Jane
  - <input type="text" id="d_jane">
* - Ike
  - <input type="text" id="d_ike">
* - Heather
  - <input type="text" id="d_heather">
* - Diane
  - <input type="text" id="d_diane">
* - ...
  - ...
```