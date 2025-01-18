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

**110** channels, **1,234,356.9** hours playtime between **2023-01-17** and **2025-01-19**


### playtime per genre (top 30)

    80778.3h 6.54% Nachrichten
    55790.1h 4.52% Verkaufsshow
    51174.7h 4.15% Krimiserie
    45874.0h 3.72% Werbesendung
    38378.6h 3.11% Dokureihe
    36266.1h 2.94% Dokusoap
    35916.2h 2.91% Regionalmagazin
    32935.6h 2.67% Dokumentation
    29387.9h 2.38% *unknown*
    23242.0h 1.88% Zeichentrickserie
    22861.9h 1.85% Infomercial
    22068.8h 1.79% Animationsserie
    17314.7h 1.40% Comedyserie
    17227.9h 1.40% Morgenmagazin
    16276.8h 1.32% Talkshow
    16092.7h 1.30% Religionsmagazin
    14979.0h 1.21% Magazin
    12234.3h 0.99% E-Sport
    11822.1h 0.96% Sitcom
    11305.3h 0.92% Komödie
    11181.0h 0.91% Wetterbericht
    10953.1h 0.89% Quiz
    10824.6h 0.88% Programmende
    9556.2h  0.77% Realityshow
    9406.9h  0.76% Politikmagazin
    9130.8h  0.74% Wissensmagazin
    8813.6h  0.71% Börsenmagazin
    8183.1h  0.66% Dramaserie
    8171.9h  0.66% Arztserie
    8160.1h  0.66% Wirtschaftsmagazin
