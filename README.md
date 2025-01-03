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

**110** channels, **1,211,832.9** hours playtime between **2023-01-17** and **2025-01-04**


### playtime per genre (top 30)

    79191.2h 6.53% Nachrichten
    54935.6h 4.53% Verkaufsshow
    50253.6h 4.15% Krimiserie
    44895.9h 3.70% Werbesendung
    37718.1h 3.11% Dokureihe
    35648.1h 2.94% Dokusoap
    35310.8h 2.91% Regionalmagazin
    32248.8h 2.66% Dokumentation
    28798.5h 2.38% *unknown*
    22768.5h 1.88% Zeichentrickserie
    22419.8h 1.85% Infomercial
    21639.9h 1.79% Animationsserie
    17088.9h 1.41% Comedyserie
    16910.7h 1.40% Morgenmagazin
    15977.9h 1.32% Talkshow
    15886.9h 1.31% Religionsmagazin
    14811.7h 1.22% Magazin
    11982.0h 0.99% E-Sport
    11605.7h 0.96% Sitcom
    11098.1h 0.92% Komödie
    10963.3h 0.90% Wetterbericht
    10724.3h 0.88% Quiz
    10652.7h 0.88% Programmende
    9359.7h  0.77% Realityshow
    9225.2h  0.76% Politikmagazin
    9008.1h  0.74% Wissensmagazin
    8745.3h  0.72% Börsenmagazin
    8028.7h  0.66% Wirtschaftsmagazin
    8018.6h  0.66% Arztserie
    8014.6h  0.66% Dramaserie
