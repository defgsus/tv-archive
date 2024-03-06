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

**99** channels, **743,042.0** hours playtime between **2023-01-17** and **2024-03-07**


### playtime per genre (top 30)

    48353.8h 6.51% Nachrichten
    35677.0h 4.80% Verkaufsshow
    30228.8h 4.07% Krimiserie
    25721.5h 3.46% Werbesendung
    23746.2h 3.20% Dokureihe
    22451.9h 3.02% Dokusoap
    21567.0h 2.90% Regionalmagazin
    19134.8h 2.58% Dokumentation
    19076.5h 2.57% *unknown*
    13748.5h 1.85% Zeichentrickserie
    13511.2h 1.82% Infomercial
    13098.8h 1.76% Animationsserie
    11269.8h 1.52% Comedyserie
    10546.0h 1.42% Morgenmagazin
    10043.1h 1.35% Religionsmagazin
    10036.0h 1.35% Magazin
    9885.0h  1.33% Talkshow
    7338.1h  0.99% E-Sport
    7042.2h  0.95% Programmende
    7004.4h  0.94% Sitcom
    6636.1h  0.89% Börsenmagazin
    6607.5h  0.89% Wetterbericht
    6303.6h  0.85% Komödie
    6282.3h  0.85% Quiz
    5557.9h  0.75% Wissensmagazin
    5405.5h  0.73% Realityshow
    5382.9h  0.72% Wirtschaftsmagazin
    5361.0h  0.72% Politikmagazin
    5305.8h  0.71% Telenovela
    5087.2h  0.68% Musikmagazin
