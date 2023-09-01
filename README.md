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

**97** channels, **410,957.2** hours playtime between **2023-01-17** and **2023-09-02**


### playtime per genre (top 30)

    27166.8h 6.61% Nachrichten
    19449.8h 4.73% Verkaufsshow
    16685.1h 4.06% Krimiserie
    13848.2h 3.37% Werbesendung
    13586.3h 3.31% Dokureihe
    12484.2h 3.04% Dokusoap
    11843.0h 2.88% Regionalmagazin
    10392.8h 2.53% Dokumentation
    9893.0h  2.41% *unknown*
    7747.9h  1.89% Zeichentrickserie
    7505.1h  1.83% Infomercial
    7273.1h  1.77% Animationsserie
    6695.3h  1.63% Comedyserie
    5814.2h  1.41% Morgenmagazin
    5481.9h  1.33% Religionsmagazin
    5406.5h  1.32% Talkshow
    5125.2h  1.25% Magazin
    4480.8h  1.09% Programmende
    4071.7h  0.99% E-Sport
    3889.7h  0.95% Wetterbericht
    3850.1h  0.94% Sitcom
    3714.8h  0.90% Börsenmagazin
    3360.4h  0.82% Quiz
    3258.8h  0.79% Musikmagazin
    3196.3h  0.78% Komödie
    3128.8h  0.76% Wirtschaftsmagazin
    3074.8h  0.75% Wissensmagazin
    2894.8h  0.70% Telenovela
    2706.1h  0.66% Reportagereihe
    2659.4h  0.65% Politikmagazin
