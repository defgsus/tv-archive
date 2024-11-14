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

**109** channels, **1,139,573.9** hours playtime between **2023-01-17** and **2024-11-15**


### playtime per genre (top 30)

    74295.8h 6.52% Nachrichten
    52160.8h 4.58% Verkaufsshow
    47496.2h 4.17% Krimiserie
    41903.0h 3.68% Werbesendung
    35565.3h 3.12% Dokureihe
    34002.2h 2.98% Dokusoap
    33352.3h 2.93% Regionalmagazin
    29940.2h 2.63% Dokumentation
    26940.8h 2.36% *unknown*
    21311.1h 1.87% Zeichentrickserie
    21005.3h 1.84% Infomercial
    20370.1h 1.79% Animationsserie
    16352.3h 1.43% Comedyserie
    15953.1h 1.40% Morgenmagazin
    15217.0h 1.34% Religionsmagazin
    15092.2h 1.32% Talkshow
    14275.5h 1.25% Magazin
    11254.4h 0.99% E-Sport
    11026.5h 0.97% Sitcom
    10310.4h 0.90% Wetterbericht
    10080.3h 0.88% Programmende
    10071.1h 0.88% Quiz
    10010.0h 0.88% Komödie
    8742.0h  0.77% Realityshow
    8653.5h  0.76% Politikmagazin
    8562.3h  0.75% Wissensmagazin
    8545.8h  0.75% Börsenmagazin
    7645.0h  0.67% Wirtschaftsmagazin
    7539.0h  0.66% Telenovela
    7497.4h  0.66% Dramaserie
