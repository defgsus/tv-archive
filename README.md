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

**110** channels, **1,215,267.6** hours playtime between **2023-01-17** and **2025-01-06**


### playtime per genre (top 30)

    79385.4h 6.53% Nachrichten
    55056.4h 4.53% Verkaufsshow
    50355.1h 4.14% Krimiserie
    45046.8h 3.71% Werbesendung
    37867.5h 3.12% Dokureihe
    35730.2h 2.94% Dokusoap
    35356.7h 2.91% Regionalmagazin
    32366.3h 2.66% Dokumentation
    28909.1h 2.38% *unknown*
    22845.5h 1.88% Zeichentrickserie
    22492.7h 1.85% Infomercial
    21707.3h 1.79% Animationsserie
    17114.0h 1.41% Comedyserie
    16928.6h 1.39% Morgenmagazin
    16026.5h 1.32% Talkshow
    15930.4h 1.31% Religionsmagazin
    14855.8h 1.22% Magazin
    12014.4h 0.99% E-Sport
    11627.5h 0.96% Sitcom
    11143.8h 0.92% Komödie
    10994.9h 0.90% Wetterbericht
    10731.5h 0.88% Quiz
    10680.2h 0.88% Programmende
    9391.3h  0.77% Realityshow
    9229.8h  0.76% Politikmagazin
    9034.6h  0.74% Wissensmagazin
    8745.2h  0.72% Börsenmagazin
    8038.9h  0.66% Wirtschaftsmagazin
    8028.3h  0.66% Dramaserie
    8024.7h  0.66% Arztserie
