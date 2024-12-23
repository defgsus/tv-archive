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

**109** channels, **1,196,179.1** hours playtime between **2023-01-17** and **2024-12-24**


### playtime per genre (top 30)

    78268.9h 6.54% Nachrichten
    54327.1h 4.54% Verkaufsshow
    49821.1h 4.17% Krimiserie
    44224.1h 3.70% Werbesendung
    37221.3h 3.11% Dokureihe
    35310.4h 2.95% Dokusoap
    35002.4h 2.93% Regionalmagazin
    31679.1h 2.65% Dokumentation
    28268.6h 2.36% *unknown*
    22436.5h 1.88% Zeichentrickserie
    22162.5h 1.85% Infomercial
    21391.8h 1.79% Animationsserie
    16926.9h 1.42% Comedyserie
    16767.8h 1.40% Morgenmagazin
    15868.0h 1.33% Talkshow
    15754.9h 1.32% Religionsmagazin
    14705.4h 1.23% Magazin
    11826.2h 0.99% E-Sport
    11494.5h 0.96% Sitcom
    10823.0h 0.90% Wetterbericht
    10635.0h 0.89% Komödie
    10595.8h 0.89% Quiz
    10537.2h 0.88% Programmende
    9225.9h  0.77% Realityshow
    9126.5h  0.76% Politikmagazin
    8937.0h  0.75% Wissensmagazin
    8719.8h  0.73% Börsenmagazin
    7970.4h  0.67% Wirtschaftsmagazin
    7948.8h  0.66% Arztserie
    7933.1h  0.66% Dramaserie
