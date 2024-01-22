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

**99** channels, **664,848.1** hours playtime between **2023-01-17** and **2024-01-23**


### playtime per genre (top 30)

    43358.8h 6.52% Nachrichten
    31806.1h 4.78% Verkaufsshow
    26711.3h 4.02% Krimiserie
    22689.6h 3.41% Werbesendung
    21618.2h 3.25% Dokureihe
    19895.6h 2.99% Dokusoap
    19155.7h 2.88% Regionalmagazin
    17228.6h 2.59% Dokumentation
    16625.7h 2.50% *unknown*
    12296.3h 1.85% Zeichentrickserie
    12071.4h 1.82% Infomercial
    11688.2h 1.76% Animationsserie
    10061.5h 1.51% Comedyserie
    9390.9h  1.41% Morgenmagazin
    8987.2h  1.35% Religionsmagazin
    8817.3h  1.33% Magazin
    8787.1h  1.32% Talkshow
    6537.5h  0.98% E-Sport
    6427.6h  0.97% Programmende
    6395.4h  0.96% Sitcom
    5987.6h  0.90% Wetterbericht
    5906.9h  0.89% Börsenmagazin
    5653.6h  0.85% Komödie
    5505.7h  0.83% Quiz
    5006.4h  0.75% Wissensmagazin
    4854.9h  0.73% Wirtschaftsmagazin
    4842.6h  0.73% Realityshow
    4717.4h  0.71% Telenovela
    4696.5h  0.71% Politikmagazin
    4694.1h  0.71% Musikmagazin
