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

**102** channels, **843,257.3** hours playtime between **2023-01-17** and **2024-05-08**


### playtime per genre (top 30)

    55021.7h 6.52% Nachrichten
    40288.2h 4.78% Verkaufsshow
    34321.2h 4.07% Krimiserie
    29490.9h 3.50% Werbesendung
    26608.7h 3.16% Dokureihe
    25462.8h 3.02% Dokusoap
    24529.0h 2.91% Regionalmagazin
    21850.5h 2.59% Dokumentation
    21496.2h 2.55% *unknown*
    15505.9h 1.84% Zeichentrickserie
    15330.7h 1.82% Infomercial
    15013.8h 1.78% Animationsserie
    12746.5h 1.51% Comedyserie
    11915.0h 1.41% Magazin
    11886.3h 1.41% Morgenmagazin
    11393.2h 1.35% Religionsmagazin
    11234.1h 1.33% Talkshow
    8371.6h  0.99% E-Sport
    7828.8h  0.93% Programmende
    7756.2h  0.92% Sitcom
    7488.9h  0.89% Wetterbericht
    7441.0h  0.88% Börsenmagazin
    7286.6h  0.86% Quiz
    7211.9h  0.86% Komödie
    6228.9h  0.74% Wissensmagazin
    6190.4h  0.73% Politikmagazin
    6176.1h  0.73% Realityshow
    6023.5h  0.71% Wirtschaftsmagazin
    6015.0h  0.71% Telenovela
    5603.2h  0.66% Musikmagazin
