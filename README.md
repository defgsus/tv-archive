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

**99** channels, **695,044.4** hours playtime between **2023-01-17** and **2024-02-09**


### playtime per genre (top 30)

    45327.9h 6.52% Nachrichten
    33335.7h 4.80% Verkaufsshow
    28108.5h 4.04% Krimiserie
    23850.3h 3.43% Werbesendung
    22422.3h 3.23% Dokureihe
    20905.2h 3.01% Dokusoap
    20117.1h 2.89% Regionalmagazin
    17941.4h 2.58% Dokumentation
    17532.8h 2.52% *unknown*
    12894.2h 1.86% Zeichentrickserie
    12630.6h 1.82% Infomercial
    12221.9h 1.76% Animationsserie
    10522.5h 1.51% Comedyserie
    9851.5h  1.42% Morgenmagazin
    9388.7h  1.35% Religionsmagazin
    9248.0h  1.33% Magazin
    9199.2h  1.32% Talkshow
    6847.6h  0.99% E-Sport
    6668.1h  0.96% Programmende
    6631.6h  0.95% Sitcom
    6208.4h  0.89% Wetterbericht
    6188.8h  0.89% Börsenmagazin
    5886.6h  0.85% Komödie
    5794.6h  0.83% Quiz
    5227.2h  0.75% Wissensmagazin
    5113.9h  0.74% Realityshow
    5069.4h  0.73% Wirtschaftsmagazin
    4975.8h  0.72% Politikmagazin
    4957.7h  0.71% Telenovela
    4845.5h  0.70% Musikmagazin
