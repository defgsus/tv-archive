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

**102** channels, **817,630.3** hours playtime between **2023-01-17** and **2024-04-20**


### playtime per genre (top 30)

    53287.4h 6.52% Nachrichten
    39238.5h 4.80% Verkaufsshow
    33315.3h 4.07% Krimiserie
    28547.3h 3.49% Werbesendung
    25868.1h 3.16% Dokureihe
    24657.8h 3.02% Dokusoap
    23804.6h 2.91% Regionalmagazin
    21153.4h 2.59% Dokumentation
    20935.4h 2.56% *unknown*
    15005.1h 1.84% Zeichentrickserie
    14844.3h 1.82% Infomercial
    14543.5h 1.78% Animationsserie
    12409.0h 1.52% Comedyserie
    11562.2h 1.41% Morgenmagazin
    11417.4h 1.40% Magazin
    11026.5h 1.35% Religionsmagazin
    10889.6h 1.33% Talkshow
    8079.7h  0.99% E-Sport
    7621.1h  0.93% Programmende
    7545.6h  0.92% Sitcom
    7256.2h  0.89% Wetterbericht
    7200.1h  0.88% Börsenmagazin
    7057.3h  0.86% Quiz
    6977.9h  0.85% Komödie
    6060.9h  0.74% Wissensmagazin
    5974.1h  0.73% Politikmagazin
    5895.5h  0.72% Realityshow
    5864.8h  0.72% Wirtschaftsmagazin
    5862.9h  0.72% Telenovela
    5465.9h  0.67% Musikmagazin
