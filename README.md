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

**109** channels, **1,101,572.7** hours playtime between **2023-01-17** and **2024-10-22**


### playtime per genre (top 30)

    71706.6h 6.51% Nachrichten
    50776.7h 4.61% Verkaufsshow
    45715.2h 4.15% Krimiserie
    40302.2h 3.66% Werbesendung
    34487.4h 3.13% Dokureihe
    32969.7h 2.99% Dokusoap
    32189.3h 2.92% Regionalmagazin
    28858.8h 2.62% Dokumentation
    26215.8h 2.38% *unknown*
    20544.6h 1.87% Zeichentrickserie
    20264.5h 1.84% Infomercial
    19710.9h 1.79% Animationsserie
    15933.8h 1.45% Comedyserie
    15406.4h 1.40% Morgenmagazin
    14863.9h 1.35% Religionsmagazin
    14558.0h 1.32% Talkshow
    14021.3h 1.27% Magazin
    10890.1h 0.99% E-Sport
    10598.9h 0.96% Sitcom
    9978.2h  0.91% Wetterbericht
    9789.7h  0.89% Programmende
    9665.1h  0.88% Komödie
    9661.2h  0.88% Quiz
    8419.2h  0.76% Börsenmagazin
    8372.3h  0.76% Realityshow
    8321.8h  0.76% Politikmagazin
    8279.0h  0.75% Wissensmagazin
    7412.8h  0.67% Wirtschaftsmagazin
    7255.3h  0.66% Telenovela
    7192.7h  0.65% Dramaserie
