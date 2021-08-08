# merge-intervals

[![Build Status](https://www.travis-ci.com/Drinkler/merge-intervals.svg?branch=main)](https://www.travis-ci.com/Drinkler/merge-intervals)

## Prerequisites

* Python 3.8.10
* pip 20.0.2

## How to use

### Main

```
python merge.py
```

### Testing

```
pip install -r requirements.txt
pytest
```

## Annahmen

* Ein Intervall besteht aus zwei Zahlenwerten
* Die Werte eines Intervalls sind aufsteigend sortiert
* Ein Intervall ist eine Liste
* Alle Intervalle befinden sich in einer Liste

## Vorgehen

Zuerst werden alle Intervalle anhand des ersten Wertes jedes Intervalls aufsteigend sortiert. Das Sortieren hat den Vorteil, dass der erste Wert eines Intervalls immer kleiner ist als der erste Wert des nächstens Intervalls. Dadurch ist ein späteres wiederholtes Durchlaufen der Intervalle nicht nötig.
```
input = [[25, 30], [2, 19], [14, 23], [4, 8]]
sorted_input = [[2, 19], [4, 8], [14, 23], [25, 30]]
```
Anschließend kann man herausfinden, ob zwei Intervalle überlappen, indem man den ersten Wert eines Intervalls mit dem letzten Wert des vorherigen Intervalls vergleicht.<br/>
Beispiele:
```
[[2, 19], [4, 8]] -> 4 <= 19 -> überlappen -> [2, 19]
[[2, 19], [14, 23]] -> 14 <= 19 -> überlappen -> [2, 23]
[[4, 8], [14, 23]] -> 14 <= 8 -> überlappen nicht -> [14, 23]
```
Die Intervalle überlappen sich, wenn der erste Wert kleiner oder gleich groß ist wie der zweite Wert. Der erste Wert des vorherigen Intervalls und der größte Wert beider Intervalle erstellen dann einen neuen Interval. Intervalle die nicht überlappen bleiben unberührt. Dieser Vorgang wird einmal über alle Intervalle ausgeführt. Das Ergebnis ist eine Liste von Intervallen welche sich nicht überlappen.
```
output = [[2, 23], [25, 30]]
```

## Zeitliche Komplexität

Das Sortieren, mit der Python List [`sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort) Funktion, verwendet den [Timsort Algorithmus](https://en.wikipedia.org/wiki/Timsort). Dieser hat eine Best-Case-Komplexität von O(n) und eine Worst- und Average-Case-Komplexität von O(n log(n)).<br/>
Das Durchlaufen der Liste hat eine zeitliche Komplexität von O(n).<br/>
Daher ist die Worst- und Average-Case-Gesamtkomplexität **O(n log(n))** und die Best-Case-Gesamtkomplexität **O(n)**.

## Raumkomplexität

Die Worst-Case-Raumkomplexität des Timsort Algorithmus ist O(n).<br/>
Das Durchlaufen der Liste hat eine Raumkomplexität von O(n), weil eine neue Liste angelegt wird. Wenn keine Intervalle überlappen, ist die maximale Größe der neu angelegten Liste N.<br/>
Daher ist die Gesamtraumkomplexität **O(n)**.

## Robustheit

`append()` hat ein Average-Case von O(1) und ein Amortized-Worst-Case von O(1).
`sort()` hat ein Average-Case von O(n log(n)) und ein Amortized-Worst-Case von O(n log(n)) ([Quelle](https://wiki.python.org/moin/TimeComplexity)).
D.h. mit sehr großen Eingaben kommen `sort()` und `append()` zurecht. Zu Verlangsamungen kann es kommen, wenn der Arbeitsspeicher nicht mehr ausreicht und Memory swapping eintritt.