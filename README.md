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

**97** channels, **452,001.5** hours playtime between **2023-01-17** and **2023-09-25**


### playtime per genre (top 30)

    29798.5h 6.59% Nachrichten
    21502.8h 4.76% Verkaufsshow
    18274.5h 4.04% Krimiserie
    15255.6h 3.38% Werbesendung
    14888.0h 3.29% Dokureihe
    13758.2h 3.04% Dokusoap
    12995.7h 2.88% Regionalmagazin
    11374.6h 2.52% Dokumentation
    10758.0h 2.38% *unknown*
    8515.6h  1.88% Zeichentrickserie
    8245.4h  1.82% Infomercial
    8020.1h  1.77% Animationsserie
    7289.6h  1.61% Comedyserie
    6373.6h  1.41% Morgenmagazin
    6064.0h  1.34% Religionsmagazin
    5985.9h  1.32% Talkshow
    5630.3h  1.25% Magazin
    4792.2h  1.06% Programmende
    4450.7h  0.98% E-Sport
    4253.7h  0.94% Sitcom
    4245.4h  0.94% Wetterbericht
    4059.3h  0.90% Börsenmagazin
    3760.0h  0.83% Quiz
    3504.0h  0.78% Musikmagazin
    3491.9h  0.77% Komödie
    3413.5h  0.76% Wirtschaftsmagazin
    3387.9h  0.75% Wissensmagazin
    3191.9h  0.71% Telenovela
    2985.9h  0.66% Politikmagazin
    2959.8h  0.65% Reportagereihe
