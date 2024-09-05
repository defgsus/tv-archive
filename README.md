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

**109** channels, **1,032,440.6** hours playtime between **2023-01-17** and **2024-09-06**


### playtime per genre (top 30)

    67198.2h 6.51% Nachrichten
    47997.3h 4.65% Verkaufsshow
    42520.7h 4.12% Krimiserie
    37357.0h 3.62% Werbesendung
    32450.2h 3.14% Dokureihe
    31124.4h 3.01% Dokusoap
    30148.7h 2.92% Regionalmagazin
    26990.5h 2.61% Dokumentation
    24995.6h 2.42% *unknown*
    19152.1h 1.86% Zeichentrickserie
    18924.3h 1.83% Infomercial
    18502.2h 1.79% Animationsserie
    15127.4h 1.47% Comedyserie
    14476.2h 1.40% Morgenmagazin
    14027.2h 1.36% Religionsmagazin
    13598.7h 1.32% Magazin
    13556.8h 1.31% Talkshow
    10200.8h 0.99% E-Sport
    9880.5h  0.96% Sitcom
    9341.1h  0.90% Wetterbericht
    9263.1h  0.90% Programmende
    9078.7h  0.88% Komödie
    8923.6h  0.86% Quiz
    8213.5h  0.80% Börsenmagazin
    7736.3h  0.75% Politikmagazin
    7715.9h  0.75% Wissensmagazin
    7703.5h  0.75% Realityshow
    7033.9h  0.68% Wirtschaftsmagazin
    6800.2h  0.66% Telenovela
    6739.9h  0.65% Dramaserie
