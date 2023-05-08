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

**96** channels, **203,000.5** hours playtime between **2023-01-17** and **2023-05-09**


### playtime per genre (top 30)

    13702.8h 6.75% Nachrichten
    9919.4h  4.89% Verkaufsshow
    8263.5h  4.07% Krimiserie
    6756.9h  3.33% Werbesendung
    6569.2h  3.24% Dokureihe
    6028.4h  2.97% Dokusoap
    5830.6h  2.87% Regionalmagazin
    5162.4h  2.54% Dokumentation
    4967.0h  2.45% *unknown*
    3768.9h  1.86% Zeichentrickserie
    3717.5h  1.83% Infomercial
    3686.3h  1.82% Animationsserie
    3375.9h  1.66% Comedyserie
    2801.7h  1.38% Programmende
    2796.4h  1.38% Morgenmagazin
    2674.2h  1.32% Talkshow
    2659.0h  1.31% Religionsmagazin
    2263.1h  1.11% Magazin
    2043.0h  1.01% E-Sport
    1915.8h  0.94% Sitcom
    1841.4h  0.91% Börsenmagazin
    1834.3h  0.90% Wetterbericht
    1606.0h  0.79% Wirtschaftsmagazin
    1587.2h  0.78% Wissensmagazin
    1566.4h  0.77% Musikmagazin
    1552.1h  0.76% Quiz
    1426.2h  0.70% Telenovela
    1420.0h  0.70% Sportmagazin
    1394.8h  0.69% Gesundheitsmagazin
    1381.6h  0.68% Dramaserie
