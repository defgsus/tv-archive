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

**109** channels, **943,360.7** hours playtime between **2023-01-17** and **2024-07-11**


### playtime per genre (top 30)

    61507.1h 6.52% Nachrichten
    44129.2h 4.68% Verkaufsshow
    38594.7h 4.09% Krimiserie
    33594.7h 3.56% Werbesendung
    29668.8h 3.15% Dokureihe
    28560.6h 3.03% Dokusoap
    27447.8h 2.91% Regionalmagazin
    24474.1h 2.59% Dokumentation
    23545.5h 2.50% *unknown*
    17396.4h 1.84% Zeichentrickserie
    17223.6h 1.83% Infomercial
    16871.8h 1.79% Animationsserie
    14047.8h 1.49% Comedyserie
    13355.8h 1.42% Magazin
    13297.8h 1.41% Morgenmagazin
    12789.5h 1.36% Religionsmagazin
    12499.0h 1.32% Talkshow
    9340.6h  0.99% E-Sport
    8883.9h  0.94% Sitcom
    8579.2h  0.91% Programmende
    8444.5h  0.90% Wetterbericht
    8186.8h  0.87% Komödie
    8154.2h  0.86% Quiz
    7922.4h  0.84% Börsenmagazin
    7119.0h  0.75% Politikmagazin
    7025.6h  0.74% Realityshow
    7011.6h  0.74% Wissensmagazin
    6570.1h  0.70% Wirtschaftsmagazin
    6387.6h  0.68% Telenovela
    6146.5h  0.65% Dramaserie
