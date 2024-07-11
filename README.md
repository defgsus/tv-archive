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

**109** channels, **945,185.5** hours playtime between **2023-01-17** and **2024-07-12**


### playtime per genre (top 30)

    61631.5h 6.52% Nachrichten
    44202.4h 4.68% Verkaufsshow
    38687.6h 4.09% Krimiserie
    33671.2h 3.56% Werbesendung
    29731.9h 3.15% Dokureihe
    28610.8h 3.03% Dokusoap
    27513.2h 2.91% Regionalmagazin
    24530.9h 2.60% Dokumentation
    23590.0h 2.50% *unknown*
    17434.0h 1.84% Zeichentrickserie
    17257.9h 1.83% Infomercial
    16907.0h 1.79% Animationsserie
    14085.5h 1.49% Comedyserie
    13367.7h 1.41% Magazin
    13333.6h 1.41% Morgenmagazin
    12814.8h 1.36% Religionsmagazin
    12515.2h 1.32% Talkshow
    9359.3h  0.99% E-Sport
    8902.6h  0.94% Sitcom
    8592.9h  0.91% Programmende
    8463.3h  0.90% Wetterbericht
    8187.1h  0.87% Komödie
    8174.9h  0.86% Quiz
    7931.6h  0.84% Börsenmagazin
    7138.0h  0.76% Politikmagazin
    7045.8h  0.75% Realityshow
    7026.1h  0.74% Wissensmagazin
    6583.8h  0.70% Wirtschaftsmagazin
    6394.4h  0.68% Telenovela
    6162.0h  0.65% Dramaserie
