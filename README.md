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

**109** channels, **925,265.1** hours playtime between **2023-01-17** and **2024-06-30**


### playtime per genre (top 30)

    60404.1h 6.53% Nachrichten
    43432.1h 4.69% Verkaufsshow
    37783.8h 4.08% Krimiserie
    32802.1h 3.55% Werbesendung
    29099.1h 3.14% Dokureihe
    28003.2h 3.03% Dokusoap
    26898.6h 2.91% Regionalmagazin
    24008.3h 2.59% Dokumentation
    23169.7h 2.50% *unknown*
    17042.9h 1.84% Zeichentrickserie
    16877.5h 1.82% Infomercial
    16531.3h 1.79% Animationsserie
    13825.9h 1.49% Comedyserie
    13216.2h 1.43% Magazin
    13034.1h 1.41% Morgenmagazin
    12534.3h 1.35% Religionsmagazin
    12300.8h 1.33% Talkshow
    9158.5h  0.99% E-Sport
    8677.0h  0.94% Sitcom
    8448.1h  0.91% Programmende
    8269.2h  0.89% Wetterbericht
    8014.2h  0.87% Komödie
    7993.8h  0.86% Quiz
    7860.7h  0.85% Börsenmagazin
    6963.4h  0.75% Politikmagazin
    6867.9h  0.74% Realityshow
    6865.8h  0.74% Wissensmagazin
    6470.3h  0.70% Wirtschaftsmagazin
    6337.2h  0.68% Telenovela
    6058.0h  0.65% Musikmagazin
