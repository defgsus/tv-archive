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

**110** channels, **1,227,377.1** hours playtime between **2023-01-17** and **2025-01-14**


### playtime per genre (top 30)

    80273.3h 6.54% Nachrichten
    55493.8h 4.52% Verkaufsshow
    50873.4h 4.14% Krimiserie
    45580.0h 3.71% Werbesendung
    38214.1h 3.11% Dokureihe
    36068.1h 2.94% Dokusoap
    35703.2h 2.91% Regionalmagazin
    32713.5h 2.67% Dokumentation
    29226.7h 2.38% *unknown*
    23099.6h 1.88% Zeichentrickserie
    22728.0h 1.85% Infomercial
    21932.8h 1.79% Animationsserie
    17242.7h 1.40% Comedyserie
    17118.1h 1.39% Morgenmagazin
    16178.7h 1.32% Talkshow
    16038.1h 1.31% Religionsmagazin
    14944.4h 1.22% Magazin
    12150.3h 0.99% E-Sport
    11752.0h 0.96% Sitcom
    11266.3h 0.92% Komödie
    11112.6h 0.91% Wetterbericht
    10887.1h 0.89% Quiz
    10768.9h 0.88% Programmende
    9500.8h  0.77% Realityshow
    9344.4h  0.76% Politikmagazin
    9098.2h  0.74% Wissensmagazin
    8788.5h  0.72% Börsenmagazin
    8120.8h  0.66% Dramaserie
    8117.2h  0.66% Wirtschaftsmagazin
    8117.0h  0.66% Arztserie
