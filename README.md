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

**110** channels, **1,241,246.3** hours playtime between **2023-01-17** and **2025-01-23**


### playtime per genre (top 30)

    81278.7h 6.55% Nachrichten
    56010.3h 4.51% Verkaufsshow
    51474.0h 4.15% Krimiserie
    46170.7h 3.72% Werbesendung
    38582.4h 3.11% Dokureihe
    36466.9h 2.94% Dokusoap
    36132.2h 2.91% Regionalmagazin
    33135.4h 2.67% Dokumentation
    29611.3h 2.39% *unknown*
    23380.7h 1.88% Zeichentrickserie
    22991.0h 1.85% Infomercial
    22191.1h 1.79% Animationsserie
    17394.8h 1.40% Comedyserie
    17337.6h 1.40% Morgenmagazin
    16363.9h 1.32% Talkshow
    16160.2h 1.30% Religionsmagazin
    15018.5h 1.21% Magazin
    12307.1h 0.99% E-Sport
    11894.2h 0.96% Sitcom
    11352.3h 0.91% Komödie
    11246.6h 0.91% Wetterbericht
    11037.7h 0.89% Quiz
    10880.1h 0.88% Programmende
    9626.6h  0.78% Realityshow
    9480.5h  0.76% Politikmagazin
    9163.7h  0.74% Wissensmagazin
    8835.5h  0.71% Börsenmagazin
    8238.7h  0.66% Dramaserie
    8229.5h  0.66% Arztserie
    8203.8h  0.66% Wirtschaftsmagazin
