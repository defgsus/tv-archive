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

**110** channels, **1,218,625.4** hours playtime between **2023-01-17** and **2025-01-08**


### playtime per genre (top 30)

    79655.6h 6.54% Nachrichten
    55153.9h 4.53% Verkaufsshow
    50517.0h 4.15% Krimiserie
    45191.9h 3.71% Werbesendung
    37962.9h 3.12% Dokureihe
    35821.6h 2.94% Dokusoap
    35471.1h 2.91% Regionalmagazin
    32458.7h 2.66% Dokumentation
    28991.0h 2.38% *unknown*
    22918.4h 1.88% Zeichentrickserie
    22558.2h 1.85% Infomercial
    21771.1h 1.79% Animationsserie
    17155.6h 1.41% Comedyserie
    16991.0h 1.39% Morgenmagazin
    16052.7h 1.32% Talkshow
    15956.3h 1.31% Religionsmagazin
    14880.9h 1.22% Magazin
    12060.9h 0.99% E-Sport
    11665.1h 0.96% Sitcom
    11171.1h 0.92% Komödie
    11032.5h 0.91% Wetterbericht
    10787.3h 0.89% Quiz
    10707.7h 0.88% Programmende
    9430.6h  0.77% Realityshow
    9274.7h  0.76% Politikmagazin
    9045.9h  0.74% Wissensmagazin
    8762.5h  0.72% Börsenmagazin
    8061.8h  0.66% Wirtschaftsmagazin
    8060.0h  0.66% Dramaserie
    8055.9h  0.66% Arztserie
