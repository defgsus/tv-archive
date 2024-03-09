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

**99** channels, **748,267.7** hours playtime between **2023-01-17** and **2024-03-10**


### playtime per genre (top 30)

    48677.9h 6.51% Nachrichten
    35959.8h 4.81% Verkaufsshow
    30464.1h 4.07% Krimiserie
    25915.4h 3.46% Werbesendung
    23912.1h 3.20% Dokureihe
    22613.5h 3.02% Dokusoap
    21717.4h 2.90% Regionalmagazin
    19276.5h 2.58% Dokumentation
    19188.2h 2.56% *unknown*
    13837.0h 1.85% Zeichentrickserie
    13610.0h 1.82% Infomercial
    13202.1h 1.76% Animationsserie
    11354.5h 1.52% Comedyserie
    10618.4h 1.42% Morgenmagazin
    10117.0h 1.35% Magazin
    10104.3h 1.35% Religionsmagazin
    9959.4h  1.33% Talkshow
    7380.2h  0.99% E-Sport
    7082.6h  0.95% Programmende
    7036.4h  0.94% Sitcom
    6661.6h  0.89% Börsenmagazin
    6649.6h  0.89% Wetterbericht
    6352.8h  0.85% Komödie
    6336.0h  0.85% Quiz
    5591.9h  0.75% Wissensmagazin
    5432.1h  0.73% Realityshow
    5410.3h  0.72% Wirtschaftsmagazin
    5394.8h  0.72% Politikmagazin
    5344.3h  0.71% Telenovela
    5114.7h  0.68% Musikmagazin
