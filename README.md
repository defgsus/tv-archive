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

**109** channels, **1,096,182.1** hours playtime between **2023-01-17** and **2024-10-19**


### playtime per genre (top 30)

    71385.3h 6.51% Nachrichten
    50573.8h 4.61% Verkaufsshow
    45487.2h 4.15% Krimiserie
    40067.7h 3.66% Werbesendung
    34306.6h 3.13% Dokureihe
    32827.8h 2.99% Dokusoap
    32064.2h 2.93% Regionalmagazin
    28706.8h 2.62% Dokumentation
    26093.6h 2.38% *unknown*
    20434.9h 1.86% Zeichentrickserie
    20159.8h 1.84% Infomercial
    19608.9h 1.79% Animationsserie
    15879.9h 1.45% Comedyserie
    15353.6h 1.40% Morgenmagazin
    14803.9h 1.35% Religionsmagazin
    14480.3h 1.32% Talkshow
    13978.9h 1.28% Magazin
    10848.4h 0.99% E-Sport
    10553.8h 0.96% Sitcom
    9929.3h  0.91% Wetterbericht
    9747.9h  0.89% Programmende
    9617.1h  0.88% Quiz
    9603.7h  0.88% Komödie
    8410.8h  0.77% Börsenmagazin
    8336.2h  0.76% Realityshow
    8277.7h  0.76% Politikmagazin
    8235.0h  0.75% Wissensmagazin
    7393.4h  0.67% Wirtschaftsmagazin
    7236.0h  0.66% Telenovela
    7168.6h  0.65% Dramaserie
