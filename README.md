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

**99** channels, **666,590.9** hours playtime between **2023-01-17** and **2024-01-24**


### playtime per genre (top 30)

    43478.6h 6.52% Nachrichten
    31898.0h 4.79% Verkaufsshow
    26811.5h 4.02% Krimiserie
    22747.2h 3.41% Werbesendung
    21666.1h 3.25% Dokureihe
    19952.3h 2.99% Dokusoap
    19221.8h 2.88% Regionalmagazin
    17249.1h 2.59% Dokumentation
    16675.4h 2.50% *unknown*
    12333.9h 1.85% Zeichentrickserie
    12104.0h 1.82% Infomercial
    11716.6h 1.76% Animationsserie
    10087.4h 1.51% Comedyserie
    9425.9h  1.41% Morgenmagazin
    9008.6h  1.35% Religionsmagazin
    8845.1h  1.33% Magazin
    8811.2h  1.32% Talkshow
    6544.5h  0.98% E-Sport
    6441.4h  0.97% Programmende
    6411.5h  0.96% Sitcom
    6001.5h  0.90% Wetterbericht
    5935.2h  0.89% Börsenmagazin
    5663.2h  0.85% Komödie
    5521.3h  0.83% Quiz
    5015.7h  0.75% Wissensmagazin
    4865.3h  0.73% Wirtschaftsmagazin
    4863.3h  0.73% Realityshow
    4737.4h  0.71% Telenovela
    4716.0h  0.71% Politikmagazin
    4707.1h  0.71% Musikmagazin
