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

**101** channels, **778,143.4** hours playtime between **2023-01-17** and **2024-03-27**


### playtime per genre (top 30)

    50655.8h 6.51% Nachrichten
    37398.2h 4.81% Verkaufsshow
    31759.1h 4.08% Krimiserie
    27068.5h 3.48% Werbesendung
    24717.7h 3.18% Dokureihe
    23491.7h 3.02% Dokusoap
    22632.0h 2.91% Regionalmagazin
    20075.8h 2.58% Dokumentation
    19953.3h 2.56% *unknown*
    14334.1h 1.84% Zeichentrickserie
    14160.1h 1.82% Infomercial
    13814.9h 1.78% Animationsserie
    11810.0h 1.52% Comedyserie
    11048.1h 1.42% Morgenmagazin
    10635.0h 1.37% Magazin
    10522.8h 1.35% Religionsmagazin
    10390.0h 1.34% Talkshow
    7668.1h  0.99% E-Sport
    7317.6h  0.94% Programmende
    7265.1h  0.93% Sitcom
    6924.6h  0.89% Börsenmagazin
    6906.1h  0.89% Wetterbericht
    6656.4h  0.86% Quiz
    6542.4h  0.84% Komödie
    5807.8h  0.75% Wissensmagazin
    5663.1h  0.73% Politikmagazin
    5610.2h  0.72% Realityshow
    5608.9h  0.72% Wirtschaftsmagazin
    5574.6h  0.72% Telenovela
    5272.7h  0.68% Musikmagazin
