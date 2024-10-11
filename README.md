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

**109** channels, **1,085,241.8** hours playtime between **2023-01-17** and **2024-10-12**


### playtime per genre (top 30)

    70651.2h 6.51% Nachrichten
    50130.8h 4.62% Verkaufsshow
    44972.2h 4.14% Krimiserie
    39592.1h 3.65% Werbesendung
    33962.1h 3.13% Dokureihe
    32527.0h 3.00% Dokusoap
    31730.7h 2.92% Regionalmagazin
    28406.3h 2.62% Dokumentation
    25883.4h 2.39% *unknown*
    20191.2h 1.86% Zeichentrickserie
    19949.8h 1.84% Infomercial
    19436.4h 1.79% Animationsserie
    15760.2h 1.45% Comedyserie
    15193.0h 1.40% Morgenmagazin
    14703.6h 1.35% Religionsmagazin
    14326.8h 1.32% Talkshow
    13908.5h 1.28% Magazin
    10734.1h 0.99% E-Sport
    10445.2h 0.96% Sitcom
    9826.2h  0.91% Wetterbericht
    9664.3h  0.89% Programmende
    9516.2h  0.88% Komödie
    9504.5h  0.88% Quiz
    8377.9h  0.77% Börsenmagazin
    8207.9h  0.76% Realityshow
    8177.4h  0.75% Politikmagazin
    8152.9h  0.75% Wissensmagazin
    7330.4h  0.68% Wirtschaftsmagazin
    7158.6h  0.66% Telenovela
    7093.3h  0.65% Dramaserie
