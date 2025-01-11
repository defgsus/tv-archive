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

**110** channels, **1,223,898.6** hours playtime between **2023-01-17** and **2025-01-12**


### playtime per genre (top 30)

    80033.1h 6.54% Nachrichten
    55356.7h 4.52% Verkaufsshow
    50728.4h 4.14% Krimiserie
    45424.9h 3.71% Werbesendung
    38088.3h 3.11% Dokureihe
    35970.7h 2.94% Dokusoap
    35610.8h 2.91% Regionalmagazin
    32616.9h 2.67% Dokumentation
    29148.5h 2.38% *unknown*
    23031.3h 1.88% Zeichentrickserie
    22660.6h 1.85% Infomercial
    21870.8h 1.79% Animationsserie
    17215.2h 1.41% Comedyserie
    17073.3h 1.39% Morgenmagazin
    16128.4h 1.32% Talkshow
    15996.7h 1.31% Religionsmagazin
    14913.3h 1.22% Magazin
    12112.7h 0.99% E-Sport
    11719.3h 0.96% Sitcom
    11230.3h 0.92% Komödie
    11083.0h 0.91% Wetterbericht
    10841.8h 0.89% Quiz
    10741.8h 0.88% Programmende
    9471.4h  0.77% Realityshow
    9313.5h  0.76% Politikmagazin
    9077.7h  0.74% Wissensmagazin
    8780.3h  0.72% Börsenmagazin
    8097.9h  0.66% Dramaserie
    8095.0h  0.66% Wirtschaftsmagazin
    8094.9h  0.66% Arztserie
