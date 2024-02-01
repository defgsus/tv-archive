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

**99** channels, **682,596.2** hours playtime between **2023-01-17** and **2024-02-02**


### playtime per genre (top 30)

    44532.1h 6.52% Nachrichten
    32697.1h 4.79% Verkaufsshow
    27530.8h 4.03% Krimiserie
    23393.8h 3.43% Werbesendung
    22088.0h 3.24% Dokureihe
    20477.0h 3.00% Dokusoap
    19746.7h 2.89% Regionalmagazin
    17612.1h 2.58% Dokumentation
    17170.0h 2.52% *unknown*
    12656.0h 1.85% Zeichentrickserie
    12402.5h 1.82% Infomercial
    11994.0h 1.76% Animationsserie
    10336.8h 1.51% Comedyserie
    9670.4h  1.42% Morgenmagazin
    9218.9h  1.35% Religionsmagazin
    9070.0h  1.33% Magazin
    9027.0h  1.32% Talkshow
    6709.2h  0.98% E-Sport
    6571.8h  0.96% Programmende
    6535.0h  0.96% Sitcom
    6116.5h  0.90% Wetterbericht
    6072.5h  0.89% Börsenmagazin
    5783.8h  0.85% Komödie
    5683.4h  0.83% Quiz
    5136.4h  0.75% Wissensmagazin
    5014.8h  0.73% Realityshow
    4983.8h  0.73% Wirtschaftsmagazin
    4870.9h  0.71% Politikmagazin
    4870.3h  0.71% Telenovela
    4784.7h  0.70% Musikmagazin
