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

**97** channels, **402,129.8** hours playtime between **2023-01-17** and **2023-08-28**


### playtime per genre (top 30)

    26536.5h 6.60% Nachrichten
    18986.0h 4.72% Verkaufsshow
    16315.5h 4.06% Krimiserie
    13555.2h 3.37% Werbesendung
    13312.7h 3.31% Dokureihe
    12184.6h 3.03% Dokusoap
    11519.5h 2.86% Regionalmagazin
    10215.0h 2.54% Dokumentation
    9726.2h  2.42% *unknown*
    7584.5h  1.89% Zeichentrickserie
    7344.6h  1.83% Infomercial
    7101.6h  1.77% Animationsserie
    6536.4h  1.63% Comedyserie
    5647.4h  1.40% Morgenmagazin
    5380.3h  1.34% Religionsmagazin
    5300.4h  1.32% Talkshow
    5014.3h  1.25% Magazin
    4412.8h  1.10% Programmende
    3985.2h  0.99% E-Sport
    3804.7h  0.95% Wetterbericht
    3756.2h  0.93% Sitcom
    3625.6h  0.90% Börsenmagazin
    3259.3h  0.81% Quiz
    3188.9h  0.79% Musikmagazin
    3142.8h  0.78% Komödie
    3051.3h  0.76% Wirtschaftsmagazin
    3011.8h  0.75% Wissensmagazin
    2803.8h  0.70% Telenovela
    2650.3h  0.66% Reportagereihe
    2583.4h  0.64% Sportmagazin
