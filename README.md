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

**99** channels, **702,134.1** hours playtime between **2023-01-17** and **2024-02-13**


### playtime per genre (top 30)

    45727.6h 6.51% Nachrichten
    33689.4h 4.80% Verkaufsshow
    28379.3h 4.04% Krimiserie
    24113.5h 3.43% Werbesendung
    22625.3h 3.22% Dokureihe
    21155.2h 3.01% Dokusoap
    20292.5h 2.89% Regionalmagazin
    18099.0h 2.58% Dokumentation
    17751.6h 2.53% *unknown*
    13019.1h 1.85% Zeichentrickserie
    12761.3h 1.82% Infomercial
    12344.9h 1.76% Animationsserie
    10628.4h 1.51% Comedyserie
    9932.6h  1.41% Morgenmagazin
    9491.6h  1.35% Religionsmagazin
    9355.8h  1.33% Magazin
    9292.8h  1.32% Talkshow
    6913.3h  0.98% E-Sport
    6724.0h  0.96% Programmende
    6682.3h  0.95% Sitcom
    6259.3h  0.89% Wetterbericht
    6253.3h  0.89% Börsenmagazin
    5969.9h  0.85% Komödie
    5848.2h  0.83% Quiz
    5273.1h  0.75% Wissensmagazin
    5152.5h  0.73% Realityshow
    5109.9h  0.73% Wirtschaftsmagazin
    5012.1h  0.71% Politikmagazin
    4991.3h  0.71% Telenovela
    4882.4h  0.70% Musikmagazin
