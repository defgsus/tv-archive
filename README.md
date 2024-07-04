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

**109** channels, **934,336.7** hours playtime between **2023-01-17** and **2024-07-05**


### playtime per genre (top 30)

    60970.4h 6.53% Nachrichten
    43765.8h 4.68% Verkaufsshow
    38203.7h 4.09% Krimiserie
    33203.4h 3.55% Werbesendung
    29382.3h 3.14% Dokureihe
    28265.5h 3.03% Dokusoap
    27194.5h 2.91% Regionalmagazin
    24230.7h 2.59% Dokumentation
    23362.8h 2.50% *unknown*
    17215.4h 1.84% Zeichentrickserie
    17047.8h 1.82% Infomercial
    16710.7h 1.79% Animationsserie
    13945.4h 1.49% Comedyserie
    13326.4h 1.43% Magazin
    13183.4h 1.41% Morgenmagazin
    12659.4h 1.35% Religionsmagazin
    12395.6h 1.33% Talkshow
    9249.5h  0.99% E-Sport
    8782.3h  0.94% Sitcom
    8517.1h  0.91% Programmende
    8356.6h  0.89% Wetterbericht
    8101.6h  0.87% Komödie
    8081.8h  0.86% Quiz
    7893.7h  0.84% Börsenmagazin
    7063.3h  0.76% Politikmagazin
    6969.4h  0.75% Realityshow
    6944.6h  0.74% Wissensmagazin
    6519.9h  0.70% Wirtschaftsmagazin
    6364.5h  0.68% Telenovela
    6097.6h  0.65% Musikmagazin
