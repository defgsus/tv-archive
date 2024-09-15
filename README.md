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

**109** channels, **1,047,026.9** hours playtime between **2023-01-17** and **2024-09-16**


### playtime per genre (top 30)

    68078.2h 6.50% Nachrichten
    48604.7h 4.64% Verkaufsshow
    43166.5h 4.12% Krimiserie
    37952.4h 3.62% Werbesendung
    32904.6h 3.14% Dokureihe
    31527.1h 3.01% Dokusoap
    30542.9h 2.92% Regionalmagazin
    27388.6h 2.62% Dokumentation
    25224.5h 2.41% *unknown*
    19425.6h 1.86% Zeichentrickserie
    19216.0h 1.84% Infomercial
    18753.0h 1.79% Animationsserie
    15296.9h 1.46% Comedyserie
    14642.3h 1.40% Morgenmagazin
    14252.4h 1.36% Religionsmagazin
    13778.9h 1.32% Talkshow
    13663.4h 1.30% Magazin
    10350.8h 0.99% E-Sport
    10017.8h 0.96% Sitcom
    9473.1h  0.90% Wetterbericht
    9374.2h  0.90% Programmende
    9205.5h  0.88% Komödie
    9063.6h  0.87% Quiz
    8247.5h  0.79% Börsenmagazin
    7857.3h  0.75% Wissensmagazin
    7830.9h  0.75% Politikmagazin
    7800.5h  0.75% Realityshow
    7106.6h  0.68% Wirtschaftsmagazin
    6880.6h  0.66% Telenovela
    6800.0h  0.65% Dramaserie
