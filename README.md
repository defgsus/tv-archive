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

**109** channels, **1,146,715.9** hours playtime between **2023-01-17** and **2024-11-20**


### playtime per genre (top 30)

    74759.6h 6.52% Nachrichten
    52434.1h 4.57% Verkaufsshow
    47848.4h 4.17% Krimiserie
    42202.5h 3.68% Werbesendung
    35789.5h 3.12% Dokureihe
    34180.4h 2.98% Dokusoap
    33546.1h 2.93% Regionalmagazin
    30135.3h 2.63% Dokumentation
    27078.0h 2.36% *unknown*
    21460.5h 1.87% Zeichentrickserie
    21150.7h 1.84% Infomercial
    20487.7h 1.79% Animationsserie
    16430.9h 1.43% Comedyserie
    16029.3h 1.40% Morgenmagazin
    15298.1h 1.33% Religionsmagazin
    15185.6h 1.32% Talkshow
    14335.3h 1.25% Magazin
    11327.0h 0.99% E-Sport
    11096.7h 0.97% Sitcom
    10375.3h 0.90% Wetterbericht
    10135.9h 0.88% Programmende
    10133.4h 0.88% Quiz
    10081.8h 0.88% Komödie
    8787.8h  0.77% Realityshow
    8699.0h  0.76% Politikmagazin
    8618.2h  0.75% Wissensmagazin
    8562.0h  0.75% Börsenmagazin
    7674.2h  0.67% Wirtschaftsmagazin
    7577.2h  0.66% Telenovela
    7532.1h  0.66% Dramaserie
