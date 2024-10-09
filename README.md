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

**109** channels, **1,083,469.2** hours playtime between **2023-01-17** and **2024-10-10**


### playtime per genre (top 30)

    70522.5h 6.51% Nachrichten
    50055.8h 4.62% Verkaufsshow
    44865.2h 4.14% Krimiserie
    39517.1h 3.65% Werbesendung
    33905.1h 3.13% Dokureihe
    32473.8h 3.00% Dokusoap
    31668.8h 2.92% Regionalmagazin
    28363.0h 2.62% Dokumentation
    25862.9h 2.39% *unknown*
    20157.0h 1.86% Zeichentrickserie
    19913.3h 1.84% Infomercial
    19403.5h 1.79% Animationsserie
    15738.6h 1.45% Comedyserie
    15165.1h 1.40% Morgenmagazin
    14688.4h 1.36% Religionsmagazin
    14293.8h 1.32% Talkshow
    13891.8h 1.28% Magazin
    10719.0h 0.99% E-Sport
    10426.8h 0.96% Sitcom
    9808.1h  0.91% Wetterbericht
    9650.2h  0.89% Programmende
    9498.6h  0.88% Komödie
    9479.9h  0.87% Quiz
    8368.8h  0.77% Börsenmagazin
    8189.4h  0.76% Realityshow
    8163.9h  0.75% Politikmagazin
    8139.5h  0.75% Wissensmagazin
    7315.9h  0.68% Wirtschaftsmagazin
    7139.2h  0.66% Telenovela
    7081.2h  0.65% Dramaserie
