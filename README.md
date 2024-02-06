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

**99** channels, **691,427.2** hours playtime between **2023-01-17** and **2024-02-07**


### playtime per genre (top 30)

    45068.5h 6.52% Nachrichten
    33126.4h 4.79% Verkaufsshow
    27920.6h 4.04% Krimiserie
    23734.5h 3.43% Werbesendung
    22328.9h 3.23% Dokureihe
    20783.2h 3.01% Dokusoap
    19978.5h 2.89% Regionalmagazin
    17853.5h 2.58% Dokumentation
    17438.4h 2.52% *unknown*
    12827.3h 1.86% Zeichentrickserie
    12565.2h 1.82% Infomercial
    12159.7h 1.76% Animationsserie
    10465.2h 1.51% Comedyserie
    9784.2h  1.42% Morgenmagazin
    9345.7h  1.35% Religionsmagazin
    9180.7h  1.33% Magazin
    9154.7h  1.32% Talkshow
    6804.6h  0.98% E-Sport
    6641.6h  0.96% Programmende
    6598.3h  0.95% Sitcom
    6180.4h  0.89% Wetterbericht
    6165.9h  0.89% Börsenmagazin
    5855.4h  0.85% Komödie
    5753.5h  0.83% Quiz
    5202.5h  0.75% Wissensmagazin
    5094.3h  0.74% Realityshow
    5035.4h  0.73% Wirtschaftsmagazin
    4932.1h  0.71% Politikmagazin
    4920.0h  0.71% Telenovela
    4829.2h  0.70% Musikmagazin
