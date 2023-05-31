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

**96** channels, **244,332.1** hours playtime between **2023-01-17** and **2023-06-01**


### playtime per genre (top 30)

    16334.0h 6.69% Nachrichten
    11801.3h 4.83% Verkaufsshow
    9818.7h  4.02% Krimiserie
    8114.8h  3.32% Werbesendung
    7954.9h  3.26% Dokureihe
    7282.1h  2.98% Dokusoap
    6992.1h  2.86% Regionalmagazin
    6282.4h  2.57% Dokumentation
    6059.6h  2.48% *unknown*
    4585.9h  1.88% Zeichentrickserie
    4471.9h  1.83% Infomercial
    4374.5h  1.79% Animationsserie
    4079.6h  1.67% Comedyserie
    3374.8h  1.38% Morgenmagazin
    3213.3h  1.32% Talkshow
    3199.2h  1.31% Religionsmagazin
    3196.2h  1.31% Programmende
    2816.1h  1.15% Magazin
    2440.6h  1.00% E-Sport
    2296.4h  0.94% Sitcom
    2234.2h  0.91% Börsenmagazin
    2225.4h  0.91% Wetterbericht
    1919.6h  0.79% Wirtschaftsmagazin
    1896.1h  0.78% Wissensmagazin
    1890.2h  0.77% Musikmagazin
    1890.0h  0.77% Quiz
    1771.1h  0.72% Komödie
    1719.9h  0.70% Telenovela
    1698.6h  0.70% Sportmagazin
    1622.4h  0.66% Gesundheitsmagazin
