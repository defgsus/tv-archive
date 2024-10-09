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

**109** channels, **1,083,398.6** hours playtime between **2023-01-17** and **2024-10-10**


### playtime per genre (top 30)

    70513.4h 6.51% Nachrichten
    50053.6h 4.62% Verkaufsshow
    44861.8h 4.14% Krimiserie
    39516.0h 3.65% Werbesendung
    33903.5h 3.13% Dokureihe
    32467.8h 3.00% Dokusoap
    31667.6h 2.92% Regionalmagazin
    28363.0h 2.62% Dokumentation
    25854.4h 2.39% *unknown*
    20157.0h 1.86% Zeichentrickserie
    19910.8h 1.84% Infomercial
    19403.5h 1.79% Animationsserie
    15738.0h 1.45% Comedyserie
    15159.6h 1.40% Morgenmagazin
    14687.9h 1.36% Religionsmagazin
    14292.2h 1.32% Talkshow
    13890.9h 1.28% Magazin
    10718.9h 0.99% E-Sport
    10426.7h 0.96% Sitcom
    9808.0h  0.91% Wetterbericht
    9650.6h  0.89% Programmende
    9498.6h  0.88% Komödie
    9479.9h  0.88% Quiz
    8368.8h  0.77% Börsenmagazin
    8188.9h  0.76% Realityshow
    8163.6h  0.75% Politikmagazin
    8138.8h  0.75% Wissensmagazin
    7315.9h  0.68% Wirtschaftsmagazin
    7139.2h  0.66% Telenovela
    7077.8h  0.65% Dramaserie
