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

**99** channels, **732,395.3** hours playtime between **2023-01-17** and **2024-03-01**


### playtime per genre (top 30)

    47695.6h 6.51% Nachrichten
    35165.0h 4.80% Verkaufsshow
    29789.6h 4.07% Krimiserie
    25315.4h 3.46% Werbesendung
    23436.0h 3.20% Dokureihe
    22115.1h 3.02% Dokusoap
    21254.8h 2.90% Regionalmagazin
    18891.7h 2.58% Dokumentation
    18712.5h 2.55% *unknown*
    13567.1h 1.85% Zeichentrickserie
    13317.4h 1.82% Infomercial
    12895.0h 1.76% Animationsserie
    11100.0h 1.52% Comedyserie
    10397.5h 1.42% Morgenmagazin
    9894.9h  1.35% Religionsmagazin
    9858.4h  1.35% Magazin
    9720.1h  1.33% Talkshow
    7247.6h  0.99% E-Sport
    6959.4h  0.95% Programmende
    6921.5h  0.95% Sitcom
    6531.3h  0.89% Börsenmagazin
    6512.6h  0.89% Wetterbericht
    6198.8h  0.85% Komödie
    6173.9h  0.84% Quiz
    5484.6h  0.75% Wissensmagazin
    5342.8h  0.73% Realityshow
    5314.6h  0.73% Wirtschaftsmagazin
    5283.7h  0.72% Politikmagazin
    5233.2h  0.71% Telenovela
    5033.5h  0.69% Musikmagazin
