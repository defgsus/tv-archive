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

**109** channels, **1,128,710.8** hours playtime between **2023-01-17** and **2024-11-08**


### playtime per genre (top 30)

    73524.7h 6.51% Nachrichten
    51797.8h 4.59% Verkaufsshow
    46977.0h 4.16% Krimiserie
    41449.5h 3.67% Werbesendung
    35253.2h 3.12% Dokureihe
    33710.2h 2.99% Dokusoap
    33027.5h 2.93% Regionalmagazin
    29658.2h 2.63% Dokumentation
    26784.1h 2.37% *unknown*
    21102.3h 1.87% Zeichentrickserie
    20785.4h 1.84% Infomercial
    20178.5h 1.79% Animationsserie
    16217.9h 1.44% Comedyserie
    15799.7h 1.40% Morgenmagazin
    15110.6h 1.34% Religionsmagazin
    14936.0h 1.32% Talkshow
    14183.8h 1.26% Magazin
    11143.0h 0.99% E-Sport
    10907.2h 0.97% Sitcom
    10208.1h 0.90% Wetterbericht
    9995.3h  0.89% Programmende
    9951.7h  0.88% Quiz
    9918.6h  0.88% Komödie
    8649.1h  0.77% Realityshow
    8559.6h  0.76% Politikmagazin
    8513.1h  0.75% Börsenmagazin
    8479.2h  0.75% Wissensmagazin
    7576.4h  0.67% Wirtschaftsmagazin
    7461.4h  0.66% Telenovela
    7402.7h  0.66% Dramaserie
