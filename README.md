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

**109** channels, **1,081,627.0** hours playtime between **2023-01-17** and **2024-10-09**


### playtime per genre (top 30)

    70381.9h 6.51% Nachrichten
    49981.7h 4.62% Verkaufsshow
    44778.8h 4.14% Krimiserie
    39438.3h 3.65% Werbesendung
    33865.8h 3.13% Dokureihe
    32408.9h 3.00% Dokusoap
    31598.3h 2.92% Regionalmagazin
    28328.5h 2.62% Dokumentation
    25833.7h 2.39% *unknown*
    20119.8h 1.86% Zeichentrickserie
    19874.9h 1.84% Infomercial
    19373.3h 1.79% Animationsserie
    15709.8h 1.45% Comedyserie
    15131.7h 1.40% Morgenmagazin
    14677.0h 1.36% Religionsmagazin
    14273.9h 1.32% Talkshow
    13885.5h 1.28% Magazin
    10696.5h 0.99% E-Sport
    10404.2h 0.96% Sitcom
    9788.6h  0.90% Wetterbericht
    9635.9h  0.89% Programmende
    9488.4h  0.88% Komödie
    9457.0h  0.87% Quiz
    8359.8h  0.77% Börsenmagazin
    8155.3h  0.75% Realityshow
    8135.5h  0.75% Politikmagazin
    8124.2h  0.75% Wissensmagazin
    7301.1h  0.68% Wirtschaftsmagazin
    7122.5h  0.66% Telenovela
    7056.1h  0.65% Dramaserie
