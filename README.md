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

**109** channels, **972,284.6** hours playtime between **2023-01-17** and **2024-07-30**


### playtime per genre (top 30)

    63278.9h 6.51% Nachrichten
    45386.3h 4.67% Verkaufsshow
    39857.5h 4.10% Krimiserie
    34832.6h 3.58% Werbesendung
    30596.0h 3.15% Dokureihe
    29437.9h 3.03% Dokusoap
    28280.8h 2.91% Regionalmagazin
    25284.5h 2.60% Dokumentation
    24085.4h 2.48% *unknown*
    18000.0h 1.85% Zeichentrickserie
    17780.1h 1.83% Infomercial
    17396.3h 1.79% Animationsserie
    14410.7h 1.48% Comedyserie
    13663.6h 1.41% Morgenmagazin
    13436.0h 1.38% Magazin
    13209.5h 1.36% Religionsmagazin
    12826.0h 1.32% Talkshow
    9626.3h  0.99% E-Sport
    9196.8h  0.95% Sitcom
    8800.9h  0.91% Programmende
    8733.0h  0.90% Wetterbericht
    8503.2h  0.87% Komödie
    8385.7h  0.86% Quiz
    8010.7h  0.82% Börsenmagazin
    7307.9h  0.75% Politikmagazin
    7229.4h  0.74% Wissensmagazin
    7202.7h  0.74% Realityshow
    6707.2h  0.69% Wirtschaftsmagazin
    6471.5h  0.67% Telenovela
    6330.5h  0.65% Dramaserie
