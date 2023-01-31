# Link Communities

```{image} images/link_communities_paper.png
:alt: link_communities
:width: 300px
```

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/link_communities_example1.png
:alt: link_communities
:width: 200px
```
:::
:::{grid-item} 
Typischerweise bewegen wir uns in verschiedenen sozialen Kreisen (Arbeit, Familie, Hobby, etc.).

Diese Kreise können stark überlappen oder auch Communities in Communities bilden.
:::
::::

:::{admonition} Idee der Link Communities
Eine überlappende soziale Struktur ergibt sich eher aus Clustern von ähnlichen Links als durch ein Partition der Knoten.
:::

## Ähnlichkeiten von Links (oder auch Kanten im Netzwerk)

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/link_similarity.png
:alt: link_similarity
:width: 200px
```
:::
:::{grid-item-card} Ähnlichkeitesberechung nur zwischen Links $e_{i,k}$ und $e_{j,k}$ mit einem gemeinsamen Endpunkt $k$.

$s(e_{i,k}, e_{j,k}) = \frac{|N(i) \cap N(j)|}{|N(i) \cup N(j)|}$

$N(i)$: Nachbarn von Knoten $i$
:::
::::

## Link Clustering

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/hierarchical_clustering.png
:alt: hierarchical_clustering
:width: 200px
```
:::
:::{grid-item-card} Single Link Hierarchical Clustering

1. Starte mit jeder Kante als eigenes Cluster auf Ebene 0.
2. Finde das ähnlichste Paar von Clustern nach ihrer Distanz $s(C_x, C_y) = max_{i \in C_x, j \in C_y} s(i,j)$, d.h. die größte Ähnlichkeit zwischen zwei Kanten in $C_x$ und $C_y$ und füge diese auf Ebene 1 zu einem Cluster zusammen.
3. Wiederhole Schritt 2 bis alle Kanten zu einem gemeinsamen Cluster verschmolzen wurden. 
:::
::::

## Entstehung stark überlappender Communities

1. Bestimmung einer Schnittebene des Kanten-Cluster Dendograms, z.B. nach [Partitionsdichte](https://www.nature.com/articles/nature09182/#Sec2) der Cluster auf der entsprechenden Ebene.
2. Jeder Knoten wird nach den Clustern seiner inzidenten Kanten Communities zugeordnet.

::::{grid}
:gutter: 2

:::{grid-item}
```{image} images/hierarchical_clustering.png
:alt: hierarchical_clustering
:width: 200px
```
:::
:::{grid-item} 

```{image} images/lc2nc.png
:alt: lc2nc
:width: 200px
```

Jeder Knoten kann zu so vielen Communities gehören wie er Kanten hat.
:::
::::