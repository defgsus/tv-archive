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

**109** channels, **963,216.6** hours playtime between **2023-01-17** and **2024-07-24**


### playtime per genre (top 30)

    62736.8h 6.51% Nachrichten
    44976.8h 4.67% Verkaufsshow
    39490.5h 4.10% Krimiserie
    34423.7h 3.57% Werbesendung
    30295.3h 3.15% Dokureihe
    29164.8h 3.03% Dokusoap
    28030.2h 2.91% Regionalmagazin
    25051.8h 2.60% Dokumentation
    23965.3h 2.49% *unknown*
    17826.3h 1.85% Zeichentrickserie
    17606.6h 1.83% Infomercial
    17226.9h 1.79% Animationsserie
    14308.1h 1.49% Comedyserie
    13555.2h 1.41% Morgenmagazin
    13416.0h 1.39% Magazin
    13078.4h 1.36% Religionsmagazin
    12721.8h 1.32% Talkshow
    9548.8h  0.99% E-Sport
    9092.2h  0.94% Sitcom
    8732.0h  0.91% Programmende
    8643.6h  0.90% Wetterbericht
    8401.5h  0.87% Komödie
    8310.0h  0.86% Quiz
    7984.1h  0.83% Börsenmagazin
    7254.0h  0.75% Politikmagazin
    7156.6h  0.74% Wissensmagazin
    7151.7h  0.74% Realityshow
    6661.4h  0.69% Wirtschaftsmagazin
    6446.2h  0.67% Telenovela
    6271.6h  0.65% Dramaserie
