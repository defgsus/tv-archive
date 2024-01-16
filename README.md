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

**99** channels, **654,178.7** hours playtime between **2023-01-17** and **2024-01-17**


### playtime per genre (top 30)

    42674.2h 6.52% Nachrichten
    31247.6h 4.78% Verkaufsshow
    26271.7h 4.02% Krimiserie
    22303.8h 3.41% Werbesendung
    21268.1h 3.25% Dokureihe
    19557.1h 2.99% Dokusoap
    18823.2h 2.88% Regionalmagazin
    16983.0h 2.60% Dokumentation
    16307.8h 2.49% *unknown*
    12089.8h 1.85% Zeichentrickserie
    11869.8h 1.81% Infomercial
    11499.2h 1.76% Animationsserie
    9909.0h  1.51% Comedyserie
    9248.3h  1.41% Morgenmagazin
    8849.1h  1.35% Religionsmagazin
    8646.1h  1.32% Magazin
    8642.2h  1.32% Talkshow
    6427.5h  0.98% E-Sport
    6343.6h  0.97% Programmende
    6309.1h  0.96% Sitcom
    5915.1h  0.90% Wetterbericht
    5820.3h  0.89% Börsenmagazin
    5553.9h  0.85% Komödie
    5401.9h  0.83% Quiz
    4921.9h  0.75% Wissensmagazin
    4786.6h  0.73% Wirtschaftsmagazin
    4753.7h  0.73% Realityshow
    4656.8h  0.71% Telenovela
    4646.2h  0.71% Musikmagazin
    4604.4h  0.70% Politikmagazin
