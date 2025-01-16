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

**110** channels, **1,232,582.5** hours playtime between **2023-01-17** and **2025-01-17**


### playtime per genre (top 30)

    80686.5h 6.55% Nachrichten
    55675.3h 4.52% Verkaufsshow
    51131.7h 4.15% Krimiserie
    45810.5h 3.72% Werbesendung
    38352.1h 3.11% Dokureihe
    36218.1h 2.94% Dokusoap
    35894.4h 2.91% Regionalmagazin
    32872.0h 2.67% Dokumentation
    29331.8h 2.38% *unknown*
    23208.4h 1.88% Zeichentrickserie
    22824.0h 1.85% Infomercial
    22027.0h 1.79% Animationsserie
    17295.4h 1.40% Comedyserie
    17219.9h 1.40% Morgenmagazin
    16247.6h 1.32% Talkshow
    16077.5h 1.30% Religionsmagazin
    14978.7h 1.22% Magazin
    12215.8h 0.99% E-Sport
    11811.2h 0.96% Sitcom
    11277.2h 0.91% Komödie
    11165.2h 0.91% Wetterbericht
    10951.8h 0.89% Quiz
    10810.4h 0.88% Programmende
    9549.4h  0.77% Realityshow
    9406.4h  0.76% Politikmagazin
    9122.3h  0.74% Wissensmagazin
    8814.3h  0.72% Börsenmagazin
    8178.8h  0.66% Dramaserie
    8163.9h  0.66% Arztserie
    8159.0h  0.66% Wirtschaftsmagazin
