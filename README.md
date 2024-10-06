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

**109** channels, **1,078,093.8** hours playtime between **2023-01-17** and **2024-10-07**


### playtime per genre (top 30)

    70111.2h 6.50% Nachrichten
    49841.9h 4.62% Verkaufsshow
    44586.7h 4.14% Krimiserie
    39282.1h 3.64% Werbesendung
    33763.0h 3.13% Dokureihe
    32321.9h 3.00% Dokusoap
    31456.5h 2.92% Regionalmagazin
    28225.5h 2.62% Dokumentation
    25800.0h 2.39% *unknown*
    20045.2h 1.86% Zeichentrickserie
    19811.5h 1.84% Infomercial
    19311.2h 1.79% Animationsserie
    15668.0h 1.45% Comedyserie
    15067.9h 1.40% Morgenmagazin
    14646.9h 1.36% Religionsmagazin
    14236.4h 1.32% Talkshow
    13864.2h 1.29% Magazin
    10663.2h 0.99% E-Sport
    10355.4h 0.96% Sitcom
    9754.1h  0.90% Wetterbericht
    9610.2h  0.89% Programmende
    9464.5h  0.88% Komödie
    9400.9h  0.87% Quiz
    8342.9h  0.77% Börsenmagazin
    8106.1h  0.75% Wissensmagazin
    8099.6h  0.75% Realityshow
    8098.6h  0.75% Politikmagazin
    7276.9h  0.67% Wirtschaftsmagazin
    7086.1h  0.66% Telenovela
    7027.1h  0.65% Dramaserie
