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

**96** channels, **75,689.9** hours playtime between **2023-01-17** and **2023-02-27**


### playtime per genre (top 30)

    5323.2h 7.03% Nachrichten
    3840.2h 5.07% Verkaufsshow
    3191.4h 4.22% Krimiserie
    2573.2h 3.40% Werbesendung
    2508.9h 3.31% Dokusoap
    2266.7h 2.99% Dokureihe
    2198.0h 2.90% Regionalmagazin
    1854.0h 2.45% Dokumentation
    1807.2h 2.39% *unknown*
    1426.3h 1.88% Animationsserie
    1395.8h 1.84% Zeichentrickserie
    1384.9h 1.83% Infomercial
    1221.5h 1.61% Comedyserie
    1059.1h 1.40% Morgenmagazin
    1032.0h 1.36% Programmende
    1002.4h 1.32% Religionsmagazin
    992.3h  1.31% Talkshow
    812.4h  1.07% Magazin
    792.2h  1.05% E-Sport
    707.0h  0.93% Sitcom
    663.8h  0.88% Wetterbericht
    662.4h  0.88% Börsenmagazin
    611.2h  0.81% Wirtschaftsmagazin
    594.5h  0.79% Wissensmagazin
    560.0h  0.74% Musikmagazin
    555.9h  0.73% Quiz
    543.0h  0.72% Dramaserie
    533.5h  0.70% Gesundheitsmagazin
    507.2h  0.67% Telenovela
    486.0h  0.64% Sportmagazin
