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

**109** channels, **1,054,407.9** hours playtime between **2023-01-17** and **2024-09-21**


### playtime per genre (top 30)

    68616.1h 6.51% Nachrichten
    48923.7h 4.64% Verkaufsshow
    43535.7h 4.13% Krimiserie
    38275.6h 3.63% Werbesendung
    33082.0h 3.14% Dokureihe
    31744.2h 3.01% Dokusoap
    30818.0h 2.92% Regionalmagazin
    27573.3h 2.62% Dokumentation
    25360.7h 2.41% *unknown*
    19563.9h 1.86% Zeichentrickserie
    19352.8h 1.84% Infomercial
    18888.2h 1.79% Animationsserie
    15417.0h 1.46% Comedyserie
    14779.0h 1.40% Morgenmagazin
    14344.4h 1.36% Religionsmagazin
    13886.5h 1.32% Talkshow
    13706.4h 1.30% Magazin
    10429.2h 0.99% E-Sport
    10108.9h 0.96% Sitcom
    9546.9h  0.91% Wetterbericht
    9429.5h  0.89% Programmende
    9258.8h  0.88% Komödie
    9161.5h  0.87% Quiz
    8282.9h  0.79% Börsenmagazin
    7915.4h  0.75% Politikmagazin
    7905.6h  0.75% Wissensmagazin
    7887.7h  0.75% Realityshow
    7161.9h  0.68% Wirtschaftsmagazin
    6953.9h  0.66% Telenovela
    6878.2h  0.65% Dramaserie
