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

**109** channels, **1,208,339.4** hours playtime between **2023-01-17** and **2025-01-01**


### playtime per genre (top 30)

    78959.1h 6.53% Nachrichten
    54802.5h 4.54% Verkaufsshow
    50151.2h 4.15% Krimiserie
    44736.3h 3.70% Werbesendung
    37599.7h 3.11% Dokureihe
    35562.9h 2.94% Dokusoap
    35218.8h 2.91% Regionalmagazin
    32110.2h 2.66% Dokumentation
    28694.7h 2.37% *unknown*
    22683.3h 1.88% Zeichentrickserie
    22363.6h 1.85% Infomercial
    21585.3h 1.79% Animationsserie
    17057.0h 1.41% Comedyserie
    16868.3h 1.40% Morgenmagazin
    15956.4h 1.32% Talkshow
    15861.6h 1.31% Religionsmagazin
    14787.5h 1.22% Magazin
    11946.5h 0.99% E-Sport
    11573.2h 0.96% Sitcom
    11051.7h 0.91% Komödie
    10934.5h 0.90% Wetterbericht
    10696.6h 0.89% Quiz
    10624.9h 0.88% Programmende
    9326.9h  0.77% Realityshow
    9201.0h  0.76% Politikmagazin
    8994.1h  0.74% Wissensmagazin
    8736.3h  0.72% Börsenmagazin
    8010.8h  0.66% Wirtschaftsmagazin
    8001.6h  0.66% Arztserie
    7987.4h  0.66% Dramaserie
