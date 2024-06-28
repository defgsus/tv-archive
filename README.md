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

**109** channels, **923,433.3** hours playtime between **2023-01-17** and **2024-06-29**


### playtime per genre (top 30)

    60312.3h 6.53% Nachrichten
    43352.2h 4.69% Verkaufsshow
    37720.4h 4.08% Krimiserie
    32724.9h 3.54% Werbesendung
    29034.2h 3.14% Dokureihe
    27950.8h 3.03% Dokusoap
    26877.2h 2.91% Regionalmagazin
    23955.6h 2.59% Dokumentation
    23149.8h 2.51% *unknown*
    16997.3h 1.84% Zeichentrickserie
    16840.2h 1.82% Infomercial
    16502.4h 1.79% Animationsserie
    13801.7h 1.49% Comedyserie
    13178.5h 1.43% Magazin
    13027.1h 1.41% Morgenmagazin
    12508.7h 1.35% Religionsmagazin
    12280.0h 1.33% Talkshow
    9139.1h  0.99% E-Sport
    8658.2h  0.94% Sitcom
    8434.1h  0.91% Programmende
    8251.2h  0.89% Wetterbericht
    7983.0h  0.86% Quiz
    7980.9h  0.86% Komödie
    7860.8h  0.85% Börsenmagazin
    6960.1h  0.75% Politikmagazin
    6865.6h  0.74% Realityshow
    6852.1h  0.74% Wissensmagazin
    6467.5h  0.70% Wirtschaftsmagazin
    6336.2h  0.69% Telenovela
    6047.5h  0.65% Musikmagazin
