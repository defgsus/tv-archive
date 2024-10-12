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

**109** channels, **1,087,048.2** hours playtime between **2023-01-17** and **2024-10-13**


### playtime per genre (top 30)

    70745.8h 6.51% Nachrichten
    50202.0h 4.62% Verkaufsshow
    45040.5h 4.14% Krimiserie
    39671.4h 3.65% Werbesendung
    34042.1h 3.13% Dokureihe
    32573.4h 3.00% Dokusoap
    31754.2h 2.92% Regionalmagazin
    28450.0h 2.62% Dokumentation
    25944.3h 2.39% *unknown*
    20229.8h 1.86% Zeichentrickserie
    19987.1h 1.84% Infomercial
    19468.4h 1.79% Animationsserie
    15779.4h 1.45% Comedyserie
    15202.5h 1.40% Morgenmagazin
    14717.9h 1.35% Religionsmagazin
    14348.0h 1.32% Talkshow
    13921.0h 1.28% Magazin
    10752.1h 0.99% E-Sport
    10463.2h 0.96% Sitcom
    9843.6h  0.91% Wetterbericht
    9677.0h  0.89% Programmende
    9538.0h  0.88% Komödie
    9515.9h  0.88% Quiz
    8377.9h  0.77% Börsenmagazin
    8216.1h  0.76% Realityshow
    8180.3h  0.75% Politikmagazin
    8164.8h  0.75% Wissensmagazin
    7333.0h  0.67% Wirtschaftsmagazin
    7159.9h  0.66% Telenovela
    7103.7h  0.65% Dramaserie
