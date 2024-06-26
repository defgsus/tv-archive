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

**109** channels, **921,613.4** hours playtime between **2023-01-17** and **2024-06-27**


### playtime per genre (top 30)

    60188.6h 6.53% Nachrichten
    43285.2h 4.70% Verkaufsshow
    37615.2h 4.08% Krimiserie
    32649.3h 3.54% Werbesendung
    29000.0h 3.15% Dokureihe
    27879.4h 3.03% Dokusoap
    26815.2h 2.91% Regionalmagazin
    23941.0h 2.60% Dokumentation
    23106.0h 2.51% *unknown*
    16964.1h 1.84% Zeichentrickserie
    16804.6h 1.82% Infomercial
    16466.1h 1.79% Animationsserie
    13762.2h 1.49% Comedyserie
    13156.3h 1.43% Magazin
    12991.7h 1.41% Morgenmagazin
    12485.5h 1.35% Religionsmagazin
    12253.3h 1.33% Talkshow
    9119.4h  0.99% E-Sport
    8639.8h  0.94% Sitcom
    8420.6h  0.91% Programmende
    8233.8h  0.89% Wetterbericht
    7966.4h  0.86% Komödie
    7961.8h  0.86% Quiz
    7851.9h  0.85% Börsenmagazin
    6942.6h  0.75% Politikmagazin
    6848.9h  0.74% Realityshow
    6844.2h  0.74% Wissensmagazin
    6454.7h  0.70% Wirtschaftsmagazin
    6326.1h  0.69% Telenovela
    6034.4h  0.65% Musikmagazin
