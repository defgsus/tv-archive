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

**109** channels, **1,092,545.2** hours playtime between **2023-01-17** and **2024-10-16**


### playtime per genre (top 30)

    71123.7h 6.51% Nachrichten
    50417.9h 4.61% Verkaufsshow
    45298.4h 4.15% Krimiserie
    39909.8h 3.65% Werbesendung
    34214.8h 3.13% Dokureihe
    32715.8h 2.99% Dokusoap
    31932.0h 2.92% Regionalmagazin
    28630.3h 2.62% Dokumentation
    26039.2h 2.38% *unknown*
    20359.9h 1.86% Zeichentrickserie
    20090.0h 1.84% Infomercial
    19549.3h 1.79% Animationsserie
    15835.1h 1.45% Comedyserie
    15285.5h 1.40% Morgenmagazin
    14777.9h 1.35% Religionsmagazin
    14425.2h 1.32% Talkshow
    13958.3h 1.28% Magazin
    10813.4h 0.99% E-Sport
    10511.9h 0.96% Sitcom
    9892.6h  0.91% Wetterbericht
    9719.2h  0.89% Programmende
    9585.0h  0.88% Komödie
    9573.0h  0.88% Quiz
    8394.8h  0.77% Börsenmagazin
    8281.4h  0.76% Realityshow
    8231.6h  0.75% Politikmagazin
    8209.3h  0.75% Wissensmagazin
    7362.6h  0.67% Wirtschaftsmagazin
    7197.6h  0.66% Telenovela
    7133.9h  0.65% Dramaserie
