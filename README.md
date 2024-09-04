# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**109** channels, **1,030,650.6** hours playtime between **2023-01-17** and **2024-09-05**


### playtime per genre (top 30)

    67062.0h 6.51% Nachrichten
    47920.8h 4.65% Verkaufsshow
    42452.3h 4.12% Krimiserie
    37278.7h 3.62% Werbesendung
    32387.6h 3.14% Dokureihe
    31081.7h 3.02% Dokusoap
    30076.8h 2.92% Regionalmagazin
    26931.1h 2.61% Dokumentation
    24978.7h 2.42% *unknown*
    19119.6h 1.86% Zeichentrickserie
    18889.9h 1.83% Infomercial
    18468.8h 1.79% Animationsserie
    15099.7h 1.47% Comedyserie
    14446.8h 1.40% Morgenmagazin
    14008.9h 1.36% Religionsmagazin
    13592.7h 1.32% Magazin
    13534.4h 1.31% Talkshow
    10185.9h 0.99% E-Sport
    9858.5h  0.96% Sitcom
    9323.5h  0.90% Wetterbericht
    9249.0h  0.90% Programmende
    9062.9h  0.88% Komödie
    8903.0h  0.86% Quiz
    8204.5h  0.80% Börsenmagazin
    7716.0h  0.75% Politikmagazin
    7697.3h  0.75% Wissensmagazin
    7669.2h  0.74% Realityshow
    7018.1h  0.68% Wirtschaftsmagazin
    6783.4h  0.66% Telenovela
    6720.6h  0.65% Dramaserie
