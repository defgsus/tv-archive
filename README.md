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

**96** channels, **215,651.1** hours playtime between **2023-01-17** and **2023-05-16**


### playtime per genre (top 30)

    14531.7h 6.74% Nachrichten
    10478.8h 4.86% Verkaufsshow
    8760.8h  4.06% Krimiserie
    7166.1h  3.32% Werbesendung
    7007.0h  3.25% Dokureihe
    6373.8h  2.96% Dokusoap
    6189.9h  2.87% Regionalmagazin
    5483.6h  2.54% Dokumentation
    5333.1h  2.47% *unknown*
    4011.4h  1.86% Zeichentrickserie
    3955.6h  1.83% Infomercial
    3895.0h  1.81% Animationsserie
    3593.6h  1.67% Comedyserie
    2982.4h  1.38% Morgenmagazin
    2976.0h  1.38% Programmende
    2851.2h  1.32% Talkshow
    2825.4h  1.31% Religionsmagazin
    2454.0h  1.14% Magazin
    2167.3h  1.01% E-Sport
    2039.0h  0.95% Sitcom
    1963.6h  0.91% Börsenmagazin
    1951.7h  0.91% Wetterbericht
    1705.5h  0.79% Wirtschaftsmagazin
    1687.9h  0.78% Wissensmagazin
    1663.4h  0.77% Musikmagazin
    1659.3h  0.77% Quiz
    1517.4h  0.70% Telenovela
    1503.9h  0.70% Sportmagazin
    1474.3h  0.68% Komödie
    1463.8h  0.68% Gesundheitsmagazin
