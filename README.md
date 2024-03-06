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

**99** channels, **743,018.1** hours playtime between **2023-01-17** and **2024-03-07**


### playtime per genre (top 30)

    48362.0h 6.51% Nachrichten
    35676.8h 4.80% Verkaufsshow
    30229.2h 4.07% Krimiserie
    25721.5h 3.46% Werbesendung
    23742.7h 3.20% Dokureihe
    22452.5h 3.02% Dokusoap
    21567.0h 2.90% Regionalmagazin
    19133.9h 2.58% Dokumentation
    19076.9h 2.57% *unknown*
    13748.5h 1.85% Zeichentrickserie
    13511.2h 1.82% Infomercial
    13098.8h 1.76% Animationsserie
    11269.9h 1.52% Comedyserie
    10545.5h 1.42% Morgenmagazin
    10043.1h 1.35% Religionsmagazin
    10035.1h 1.35% Magazin
    9885.7h  1.33% Talkshow
    7338.1h  0.99% E-Sport
    7042.2h  0.95% Programmende
    7004.2h  0.94% Sitcom
    6635.9h  0.89% Börsenmagazin
    6603.7h  0.89% Wetterbericht
    6304.0h  0.85% Komödie
    6281.2h  0.85% Quiz
    5557.0h  0.75% Wissensmagazin
    5405.5h  0.73% Realityshow
    5382.9h  0.72% Wirtschaftsmagazin
    5363.0h  0.72% Politikmagazin
    5305.8h  0.71% Telenovela
    5087.2h  0.68% Musikmagazin
