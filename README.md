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

**109** channels, **1,141,345.7** hours playtime between **2023-01-17** and **2024-11-17**


### playtime per genre (top 30)

    74385.0h 6.52% Nachrichten
    52232.8h 4.58% Verkaufsshow
    47578.6h 4.17% Krimiserie
    41976.2h 3.68% Werbesendung
    35626.5h 3.12% Dokureihe
    34030.8h 2.98% Dokusoap
    33376.9h 2.92% Regionalmagazin
    29985.9h 2.63% Dokumentation
    26977.1h 2.36% *unknown*
    21347.9h 1.87% Zeichentrickserie
    21043.0h 1.84% Infomercial
    20403.4h 1.79% Animationsserie
    16376.0h 1.43% Comedyserie
    15957.1h 1.40% Morgenmagazin
    15236.7h 1.33% Religionsmagazin
    15121.0h 1.32% Talkshow
    14294.5h 1.25% Magazin
    11266.8h 0.99% E-Sport
    11040.9h 0.97% Sitcom
    10325.6h 0.90% Wetterbericht
    10094.0h 0.88% Programmende
    10076.7h 0.88% Quiz
    10034.6h 0.88% Komödie
    8724.6h  0.76% Realityshow
    8651.3h  0.76% Politikmagazin
    8573.5h  0.75% Wissensmagazin
    8545.2h  0.75% Börsenmagazin
    7643.7h  0.67% Wirtschaftsmagazin
    7539.7h  0.66% Telenovela
    7486.9h  0.66% Dramaserie
