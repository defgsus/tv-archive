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

**99** channels, **661,311.7** hours playtime between **2023-01-17** and **2024-01-21**


### playtime per genre (top 30)

    43143.6h 6.52% Nachrichten
    31617.1h 4.78% Verkaufsshow
    26584.6h 4.02% Krimiserie
    22568.1h 3.41% Werbesendung
    21478.6h 3.25% Dokureihe
    19766.7h 2.99% Dokusoap
    19049.1h 2.88% Regionalmagazin
    17137.5h 2.59% Dokumentation
    16503.2h 2.50% *unknown*
    12223.6h 1.85% Zeichentrickserie
    12007.8h 1.82% Infomercial
    11629.2h 1.76% Animationsserie
    10014.8h 1.51% Comedyserie
    9354.4h  1.41% Morgenmagazin
    8934.0h  1.35% Religionsmagazin
    8763.1h  1.33% Magazin
    8737.0h  1.32% Talkshow
    6506.1h  0.98% E-Sport
    6398.2h  0.97% Programmende
    6364.3h  0.96% Sitcom
    5966.4h  0.90% Wetterbericht
    5877.8h  0.89% Börsenmagazin
    5629.6h  0.85% Komödie
    5471.5h  0.83% Quiz
    4976.1h  0.75% Wissensmagazin
    4835.0h  0.73% Wirtschaftsmagazin
    4812.9h  0.73% Realityshow
    4704.3h  0.71% Telenovela
    4676.8h  0.71% Musikmagazin
    4667.0h  0.71% Politikmagazin
