# Closeness centrality

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/kite_graph.png
:alt: kite_graph
:width: 300px
```
:::

:::{grid-item-card} Closeness centrality = Global importance
Measure in how many steps all others can be reached. 
In addition to direct exchange power also comes from acting 
as a "reference point" by which other actors judge themselves, 
and by being a center of attention who's views are heard 
by larger numbers of actors. 

Actors who are able to reach other actors at shorter 
path lengths, or who are more reachable by other actors 
have favoured positions.
:::
::::

## Definition

Closeness centrality $c_C(a)$ eines Knotens $a$ ist die inverse Summe der Distanzen zu allen anderen Knoten im Netzwerk.

:::{admonition} Closeness centrality $c_C(a)$ von Akteur $a$
$c_C(a) = \sum_{i \in V} \frac{1}{d(a, i)}$

$d(a, i)$: Distanz, d.h. Länge des kürzesten Pfades zwischen $a$ und $i$.
:::

In gerichteten Netzwerken wird wieder zwischen ausgehenden und eingehenden Kanten unterschieden.

## Beispiel

```{image} images/kite_graph.png
:alt: kite_graph
:width: 300px
```

```{list-table}
:header-rows: 1

* - $a$
  - $c_C(a)$
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

## Berühmte Beispiele

::::{grid}
:gutter: 2

:::{grid-item-card} Erdös-Zahl
Der Mathematiker Paul Erdös hat die Erdös Zahl 0. Seine direkten Co-Autoren die Erdös Zahl 1. Ko-Autoren von Co-Autoren die Zahl 2, usw.

https://www.csauthors.net/distance

```{image} images/erdos.png
:alt: kite_graph
:width: 300px
```
:::

:::{grid-item-card} Bacon-Zahl
Kevin Bacon ist ein Schauspieler mit besonders hoher Closeness Centrality im Netzwerk aus Schauspielern, die im selben Film mitgespielt haben.

https://www.oracleofbacon.org/

```{image} images/bacon.png
:alt: kite_graph
:width: 300px
``` 
:::
::::