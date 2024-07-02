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

**109** channels, **930,672.1** hours playtime between **2023-01-17** and **2024-07-03**


### playtime per genre (top 30)

    60730.0h 6.53% Nachrichten
    43640.4h 4.69% Verkaufsshow
    38041.4h 4.09% Krimiserie
    33050.7h 3.55% Werbesendung
    29276.0h 3.15% Dokureihe
    28156.7h 3.03% Dokusoap
    27060.7h 2.91% Regionalmagazin
    24123.8h 2.59% Dokumentation
    23264.2h 2.50% *unknown*
    17149.2h 1.84% Zeichentrickserie
    16976.8h 1.82% Infomercial
    16633.2h 1.79% Animationsserie
    13889.7h 1.49% Comedyserie
    13291.9h 1.43% Magazin
    13112.0h 1.41% Morgenmagazin
    12613.4h 1.36% Religionsmagazin
    12352.4h 1.33% Talkshow
    9207.5h  0.99% E-Sport
    8734.7h  0.94% Sitcom
    8489.6h  0.91% Programmende
    8319.0h  0.89% Wetterbericht
    8074.4h  0.87% Komödie
    8043.2h  0.86% Quiz
    7878.3h  0.85% Börsenmagazin
    7012.4h  0.75% Politikmagazin
    6926.9h  0.74% Realityshow
    6914.0h  0.74% Wissensmagazin
    6495.3h  0.70% Wirtschaftsmagazin
    6350.8h  0.68% Telenovela
    6080.5h  0.65% Musikmagazin
