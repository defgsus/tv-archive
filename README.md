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

**109** channels, **986,867.2** hours playtime between **2023-01-17** and **2024-08-08**


### playtime per genre (top 30)

    64212.4h 6.51% Nachrichten
    46014.1h 4.66% Verkaufsshow
    40452.4h 4.10% Krimiserie
    35435.9h 3.59% Werbesendung
    31006.3h 3.14% Dokureihe
    29849.6h 3.02% Dokusoap
    28741.6h 2.91% Regionalmagazin
    25690.3h 2.60% Dokumentation
    24297.8h 2.46% *unknown*
    18291.7h 1.85% Zeichentrickserie
    18057.7h 1.83% Infomercial
    17650.0h 1.79% Animationsserie
    14573.4h 1.48% Comedyserie
    13860.0h 1.40% Morgenmagazin
    13457.0h 1.36% Magazin
    13414.3h 1.36% Religionsmagazin
    12973.8h 1.31% Talkshow
    9776.5h  0.99% E-Sport
    9364.8h  0.95% Sitcom
    8911.0h  0.90% Programmende
    8878.4h  0.90% Wetterbericht
    8639.2h  0.88% Komödie
    8487.4h  0.86% Quiz
    8065.1h  0.82% Börsenmagazin
    7408.2h  0.75% Politikmagazin
    7341.9h  0.74% Wissensmagazin
    7305.0h  0.74% Realityshow
    6782.6h  0.69% Wirtschaftsmagazin
    6521.6h  0.66% Telenovela
    6424.9h  0.65% Dramaserie
