# Clique Percolation Method

**Ziel:** Identifikation überlappender Communities

```{image} images/overlapping_communities.jpg
:alt: overlapping_communities
:width: 500px
```

## Cliquen in Netzwerken

:::{admonition} $k$-Clique
Eine k-clique ist ein vollständig verbundener Subgraph mit $k$ Knoten.
:::

:::{admonition} Adjazente $k$-Cliquen
Zwei k-Cliquen sind adjazent wenn sie $k-1$ Knoten gemeinsam haben.

```{image} images/clique_adjacency.png
:alt: clique_adjacency
:width: 300px
```
:::

## $k$-Clique Percolation Algorithmus

**1. Finde alle maximalen Cliquen $C$ mit mindestens $k$ Knoten im Netzwerk**

```{image} images/3cliques.png
:alt: 3cliques
:width: 500px
```

**2. Identifizire adjazente Cliquen**

*Clique Graph*

```{image} images/clique_graph.png
:alt: clique_graph
:width: 500px
```

**3. Verbundene Komponenten des Clique Graph machen die Communities**

*Clique Graph*

```{image} images/cpm_result.png
:alt: clique_graph
:width: 500px
```