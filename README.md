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

**97** channels, **539,890.9** hours playtime between **2023-01-17** and **2023-11-13**


### playtime per genre (top 30)

    35503.3h 6.58% Nachrichten
    25785.9h 4.78% Verkaufsshow
    21734.1h 4.03% Krimiserie
    18311.2h 3.39% Werbesendung
    17668.8h 3.27% Dokureihe
    16377.0h 3.03% Dokusoap
    15562.0h 2.88% Regionalmagazin
    13759.0h 2.55% Dokumentation
    13109.1h 2.43% *unknown*
    10021.7h 1.86% Zeichentrickserie
    9836.7h  1.82% Infomercial
    9642.3h  1.79% Animationsserie
    8481.6h  1.57% Comedyserie
    7658.9h  1.42% Morgenmagazin
    7288.1h  1.35% Religionsmagazin
    7219.0h  1.34% Talkshow
    6851.6h  1.27% Magazin
    5471.2h  1.01% Programmende
    5300.2h  0.98% E-Sport
    5163.5h  0.96% Sitcom
    4970.4h  0.92% Wetterbericht
    4888.0h  0.91% Börsenmagazin
    4493.5h  0.83% Quiz
    4237.3h  0.78% Komödie
    4087.2h  0.76% Wissensmagazin
    4055.6h  0.75% Wirtschaftsmagazin
    4005.5h  0.74% Musikmagazin
    3878.5h  0.72% Telenovela
    3731.1h  0.69% Politikmagazin
    3682.6h  0.68% Realityshow
