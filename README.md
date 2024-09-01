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

**109** channels, **1,025,246.9** hours playtime between **2023-01-17** and **2024-09-02**


### playtime per genre (top 30)

    66661.0h 6.50% Nachrichten
    47698.3h 4.65% Verkaufsshow
    42180.1h 4.11% Krimiserie
    37049.2h 3.61% Werbesendung
    32252.0h 3.15% Dokureihe
    30932.2h 3.02% Dokusoap
    29874.8h 2.91% Regionalmagazin
    26803.8h 2.61% Dokumentation
    24914.2h 2.43% *unknown*
    19017.1h 1.85% Zeichentrickserie
    18791.0h 1.83% Infomercial
    18373.1h 1.79% Animationsserie
    15010.6h 1.46% Comedyserie
    14350.5h 1.40% Morgenmagazin
    13945.7h 1.36% Religionsmagazin
    13573.2h 1.32% Magazin
    13480.5h 1.31% Talkshow
    10131.5h 0.99% E-Sport
    9786.2h  0.95% Sitcom
    9268.5h  0.90% Wetterbericht
    9206.2h  0.90% Programmende
    9043.8h  0.88% Komödie
    8828.4h  0.86% Quiz
    8180.0h  0.80% Börsenmagazin
    7657.4h  0.75% Wissensmagazin
    7646.6h  0.75% Politikmagazin
    7621.2h  0.74% Realityshow
    6978.4h  0.68% Wirtschaftsmagazin
    6733.5h  0.66% Telenovela
    6676.1h  0.65% Dramaserie
