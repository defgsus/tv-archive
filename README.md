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

**109** channels, **914,362.6** hours playtime between **2023-01-17** and **2024-06-23**


### playtime per genre (top 30)

    59736.3h 6.53% Nachrichten
    43019.4h 4.70% Verkaufsshow
    37279.7h 4.08% Krimiserie
    32337.7h 3.54% Werbesendung
    28744.2h 3.14% Dokureihe
    27656.4h 3.02% Dokusoap
    26589.1h 2.91% Regionalmagazin
    23759.5h 2.60% Dokumentation
    22965.2h 2.51% *unknown*
    16824.8h 1.84% Zeichentrickserie
    16669.2h 1.82% Infomercial
    16327.1h 1.79% Animationsserie
    13682.0h 1.50% Comedyserie
    13040.2h 1.43% Magazin
    12876.0h 1.41% Morgenmagazin
    12381.4h 1.35% Religionsmagazin
    12177.5h 1.33% Talkshow
    9036.6h  0.99% E-Sport
    8554.6h  0.94% Sitcom
    8365.7h  0.91% Programmende
    8164.4h  0.89% Wetterbericht
    7917.4h  0.87% Komödie
    7899.7h  0.86% Quiz
    7826.9h  0.86% Börsenmagazin
    6862.9h  0.75% Politikmagazin
    6782.4h  0.74% Wissensmagazin
    6768.6h  0.74% Realityshow
    6414.3h  0.70% Wirtschaftsmagazin
    6303.8h  0.69% Telenovela
    6002.8h  0.66% Musikmagazin
