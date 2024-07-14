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

**109** channels, **948,791.5** hours playtime between **2023-01-17** and **2024-07-15**


### playtime per genre (top 30)

    61794.2h 6.51% Nachrichten
    44347.8h 4.67% Verkaufsshow
    38804.9h 4.09% Krimiserie
    33829.2h 3.57% Werbesendung
    29849.6h 3.15% Dokureihe
    28714.2h 3.03% Dokusoap
    27566.7h 2.91% Regionalmagazin
    24622.6h 2.60% Dokumentation
    23676.5h 2.50% *unknown*
    17516.1h 1.85% Zeichentrickserie
    17331.9h 1.83% Infomercial
    16970.4h 1.79% Animationsserie
    14121.7h 1.49% Comedyserie
    13375.0h 1.41% Magazin
    13341.5h 1.41% Morgenmagazin
    12868.5h 1.36% Religionsmagazin
    12570.5h 1.32% Talkshow
    9400.4h  0.99% E-Sport
    8927.4h  0.94% Sitcom
    8627.4h  0.91% Programmende
    8494.1h  0.90% Wetterbericht
    8275.3h  0.87% Komödie
    8188.1h  0.86% Quiz
    7931.2h  0.84% Börsenmagazin
    7139.4h  0.75% Politikmagazin
    7050.7h  0.74% Realityshow
    7047.4h  0.74% Wissensmagazin
    6588.9h  0.69% Wirtschaftsmagazin
    6398.6h  0.67% Telenovela
    6178.7h  0.65% Musikmagazin
