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

**99** channels, **687,924.8** hours playtime between **2023-01-17** and **2024-02-05**


### playtime per genre (top 30)

    44818.1h 6.51% Nachrichten
    32950.2h 4.79% Verkaufsshow
    27738.4h 4.03% Krimiserie
    23594.8h 3.43% Werbesendung
    22250.8h 3.23% Dokureihe
    20674.3h 3.01% Dokusoap
    19861.1h 2.89% Regionalmagazin
    17758.0h 2.58% Dokumentation
    17346.8h 2.52% *unknown*
    12759.5h 1.85% Zeichentrickserie
    12502.8h 1.82% Infomercial
    12093.6h 1.76% Animationsserie
    10403.7h 1.51% Comedyserie
    9716.8h  1.41% Morgenmagazin
    9302.0h  1.35% Religionsmagazin
    9143.7h  1.33% Magazin
    9110.9h  1.32% Talkshow
    6757.4h  0.98% E-Sport
    6612.9h  0.96% Programmende
    6567.4h  0.95% Sitcom
    6152.7h  0.89% Wetterbericht
    6125.0h  0.89% Börsenmagazin
    5854.6h  0.85% Komödie
    5713.1h  0.83% Quiz
    5180.0h  0.75% Wissensmagazin
    5059.2h  0.74% Realityshow
    5010.3h  0.73% Wirtschaftsmagazin
    4891.5h  0.71% Politikmagazin
    4886.9h  0.71% Telenovela
    4813.2h  0.70% Musikmagazin
