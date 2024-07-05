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

**109** channels, **934,331.0** hours playtime between **2023-01-17** and **2024-07-06**


### playtime per genre (top 30)

    60971.7h 6.53% Nachrichten
    43759.8h 4.68% Verkaufsshow
    38199.2h 4.09% Krimiserie
    33204.2h 3.55% Werbesendung
    29354.6h 3.14% Dokureihe
    28284.5h 3.03% Dokusoap
    27192.2h 2.91% Regionalmagazin
    24242.9h 2.59% Dokumentation
    23346.1h 2.50% *unknown*
    17218.4h 1.84% Zeichentrickserie
    17049.0h 1.82% Infomercial
    16703.7h 1.79% Animationsserie
    13945.6h 1.49% Comedyserie
    13326.3h 1.43% Magazin
    13183.4h 1.41% Morgenmagazin
    12662.8h 1.36% Religionsmagazin
    12400.9h 1.33% Talkshow
    9244.9h  0.99% E-Sport
    8780.4h  0.94% Sitcom
    8517.9h  0.91% Programmende
    8355.9h  0.89% Wetterbericht
    8099.4h  0.87% Komödie
    8078.9h  0.86% Quiz
    7895.6h  0.85% Börsenmagazin
    7048.7h  0.75% Politikmagazin
    6961.9h  0.75% Realityshow
    6937.8h  0.74% Wissensmagazin
    6521.0h  0.70% Wirtschaftsmagazin
    6367.9h  0.68% Telenovela
    6099.0h  0.65% Musikmagazin
