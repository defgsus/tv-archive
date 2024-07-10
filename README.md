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

**109** channels, **943,361.0** hours playtime between **2023-01-17** and **2024-07-11**


### playtime per genre (top 30)

    61505.7h 6.52% Nachrichten
    44124.0h 4.68% Verkaufsshow
    38594.9h 4.09% Krimiserie
    33594.7h 3.56% Werbesendung
    29668.4h 3.14% Dokureihe
    28560.5h 3.03% Dokusoap
    27447.8h 2.91% Regionalmagazin
    24474.1h 2.59% Dokumentation
    23545.2h 2.50% *unknown*
    17396.4h 1.84% Zeichentrickserie
    17223.6h 1.83% Infomercial
    16871.8h 1.79% Animationsserie
    14047.6h 1.49% Comedyserie
    13356.1h 1.42% Magazin
    13297.8h 1.41% Morgenmagazin
    12789.5h 1.36% Religionsmagazin
    12499.0h 1.32% Talkshow
    9340.6h  0.99% E-Sport
    8884.1h  0.94% Sitcom
    8579.2h  0.91% Programmende
    8444.4h  0.90% Wetterbericht
    8186.8h  0.87% Komödie
    8154.1h  0.86% Quiz
    7922.4h  0.84% Börsenmagazin
    7118.9h  0.75% Politikmagazin
    7025.4h  0.74% Realityshow
    7011.6h  0.74% Wissensmagazin
    6570.1h  0.70% Wirtschaftsmagazin
    6387.6h  0.68% Telenovela
    6146.5h  0.65% Dramaserie
