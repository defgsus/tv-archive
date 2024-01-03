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

**97** channels, **631,232.2** hours playtime between **2023-01-17** and **2024-01-04**


### playtime per genre (top 30)

    41196.3h 6.53% Nachrichten
    30199.2h 4.78% Verkaufsshow
    25244.9h 4.00% Krimiserie
    21444.7h 3.40% Werbesendung
    20497.3h 3.25% Dokureihe
    18870.8h 2.99% Dokusoap
    18125.7h 2.87% Regionalmagazin
    16385.2h 2.60% Dokumentation
    15664.0h 2.48% *unknown*
    11639.5h 1.84% Zeichentrickserie
    11442.3h 1.81% Infomercial
    11100.3h 1.76% Animationsserie
    9589.4h  1.52% Comedyserie
    8923.6h  1.41% Morgenmagazin
    8547.3h  1.35% Religionsmagazin
    8343.0h  1.32% Talkshow
    8271.0h  1.31% Magazin
    6211.8h  0.98% E-Sport
    6170.9h  0.98% Programmende
    6135.3h  0.97% Sitcom
    5747.9h  0.91% Wetterbericht
    5643.6h  0.89% Börsenmagazin
    5361.9h  0.85% Komödie
    5172.6h  0.82% Quiz
    4750.7h  0.75% Wissensmagazin
    4646.9h  0.74% Wirtschaftsmagazin
    4577.7h  0.73% Realityshow
    4534.3h  0.72% Musikmagazin
    4504.1h  0.71% Telenovela
    4444.4h  0.70% Politikmagazin
