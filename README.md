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

**97** channels, **521,910.2** hours playtime between **2023-01-17** and **2023-11-03**


### playtime per genre (top 30)

    34380.1h 6.59% Nachrichten
    24931.2h 4.78% Verkaufsshow
    20966.8h 4.02% Krimiserie
    17674.0h 3.39% Werbesendung
    17161.1h 3.29% Dokureihe
    15898.7h 3.05% Dokusoap
    15071.6h 2.89% Regionalmagazin
    13300.4h 2.55% Dokumentation
    12586.2h 2.41% *unknown*
    9717.8h  1.86% Zeichentrickserie
    9503.0h  1.82% Infomercial
    9334.4h  1.79% Animationsserie
    8247.4h  1.58% Comedyserie
    7425.1h  1.42% Morgenmagazin
    7033.7h  1.35% Religionsmagazin
    6941.1h  1.33% Talkshow
    6587.0h  1.26% Magazin
    5332.9h  1.02% Programmende
    5123.0h  0.98% E-Sport
    4992.9h  0.96% Sitcom
    4831.8h  0.93% Wetterbericht
    4714.6h  0.90% Börsenmagazin
    4369.1h  0.84% Quiz
    4077.6h  0.78% Komödie
    3949.1h  0.76% Wissensmagazin
    3937.6h  0.75% Wirtschaftsmagazin
    3901.2h  0.75% Musikmagazin
    3757.0h  0.72% Telenovela
    3611.2h  0.69% Politikmagazin
    3512.8h  0.67% Realityshow
