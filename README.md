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

**102** channels, **783,518.7** hours playtime between **2023-01-17** and **2024-03-31**


### playtime per genre (top 30)

    50972.2h 6.51% Nachrichten
    37627.4h 4.80% Verkaufsshow
    31940.5h 4.08% Krimiserie
    27285.2h 3.48% Werbesendung
    24919.4h 3.18% Dokureihe
    23614.1h 3.01% Dokusoap
    22754.2h 2.90% Regionalmagazin
    20260.3h 2.59% Dokumentation
    20121.4h 2.57% *unknown*
    14415.1h 1.84% Zeichentrickserie
    14234.9h 1.82% Infomercial
    13915.7h 1.78% Animationsserie
    11880.9h 1.52% Comedyserie
    11097.5h 1.42% Morgenmagazin
    10762.0h 1.37% Magazin
    10579.8h 1.35% Religionsmagazin
    10454.3h 1.33% Talkshow
    7716.9h  0.98% E-Sport
    7358.1h  0.94% Programmende
    7297.4h  0.93% Sitcom
    6951.6h  0.89% Wetterbericht
    6933.6h  0.88% Börsenmagazin
    6696.2h  0.85% Quiz
    6638.4h  0.85% Komödie
    5835.9h  0.74% Wissensmagazin
    5687.8h  0.73% Politikmagazin
    5631.5h  0.72% Wirtschaftsmagazin
    5621.3h  0.72% Realityshow
    5598.2h  0.71% Telenovela
    5299.8h  0.68% Musikmagazin
