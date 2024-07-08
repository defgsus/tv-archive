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

**109** channels, **939,715.9** hours playtime between **2023-01-17** and **2024-07-09**


### playtime per genre (top 30)

    61266.2h 6.52% Nachrichten
    43990.2h 4.68% Verkaufsshow
    38415.4h 4.09% Krimiserie
    33431.2h 3.56% Werbesendung
    29569.5h 3.15% Dokureihe
    28438.8h 3.03% Dokusoap
    27312.1h 2.91% Regionalmagazin
    24389.8h 2.60% Dokumentation
    23480.4h 2.50% *unknown*
    17320.4h 1.84% Zeichentrickserie
    17153.9h 1.83% Infomercial
    16804.1h 1.79% Animationsserie
    14005.2h 1.49% Comedyserie
    13341.8h 1.42% Magazin
    13227.3h 1.41% Morgenmagazin
    12743.4h 1.36% Religionsmagazin
    12458.1h 1.33% Talkshow
    9301.5h  0.99% E-Sport
    8832.4h  0.94% Sitcom
    8551.7h  0.91% Programmende
    8407.9h  0.89% Wetterbericht
    8160.1h  0.87% Komödie
    8123.8h  0.86% Quiz
    7904.4h  0.84% Börsenmagazin
    7082.2h  0.75% Politikmagazin
    6994.2h  0.74% Realityshow
    6981.4h  0.74% Wissensmagazin
    6546.1h  0.70% Wirtschaftsmagazin
    6374.2h  0.68% Telenovela
    6125.6h  0.65% Musikmagazin
