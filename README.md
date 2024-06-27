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

**109** channels, **923,433.4** hours playtime between **2023-01-17** and **2024-06-28**


### playtime per genre (top 30)

    60315.8h 6.53% Nachrichten
    43354.7h 4.69% Verkaufsshow
    37711.9h 4.08% Krimiserie
    32726.2h 3.54% Werbesendung
    29074.3h 3.15% Dokureihe
    27925.0h 3.02% Dokusoap
    26882.2h 2.91% Regionalmagazin
    23984.2h 2.60% Dokumentation
    23134.0h 2.51% *unknown*
    16997.0h 1.84% Zeichentrickserie
    16839.1h 1.82% Infomercial
    16505.2h 1.79% Animationsserie
    13796.0h 1.49% Comedyserie
    13182.1h 1.43% Magazin
    13027.1h 1.41% Morgenmagazin
    12510.0h 1.35% Religionsmagazin
    12271.4h 1.33% Talkshow
    9144.3h  0.99% E-Sport
    8658.8h  0.94% Sitcom
    8434.4h  0.91% Programmende
    8252.3h  0.89% Wetterbericht
    7983.6h  0.86% Komödie
    7981.1h  0.86% Quiz
    7860.2h  0.85% Börsenmagazin
    6973.2h  0.76% Politikmagazin
    6873.4h  0.74% Realityshow
    6857.8h  0.74% Wissensmagazin
    6466.7h  0.70% Wirtschaftsmagazin
    6333.7h  0.69% Telenovela
    6046.4h  0.65% Musikmagazin
