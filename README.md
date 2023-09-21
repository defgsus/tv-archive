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

**97** channels, **446,643.7** hours playtime between **2023-01-17** and **2023-09-22**


### playtime per genre (top 30)

    29504.0h 6.61% Nachrichten
    21246.9h 4.76% Verkaufsshow
    18071.5h 4.05% Krimiserie
    15069.6h 3.37% Werbesendung
    14709.9h 3.29% Dokureihe
    13595.0h 3.04% Dokusoap
    12880.9h 2.88% Regionalmagazin
    11231.2h 2.51% Dokumentation
    10618.0h 2.38% *unknown*
    8416.9h  1.88% Zeichentrickserie
    8148.9h  1.82% Infomercial
    7927.1h  1.77% Animationsserie
    7239.2h  1.62% Comedyserie
    6328.2h  1.42% Morgenmagazin
    5975.8h  1.34% Religionsmagazin
    5913.9h  1.32% Talkshow
    5575.8h  1.25% Magazin
    4757.6h  1.07% Programmende
    4398.5h  0.98% E-Sport
    4214.8h  0.94% Sitcom
    4204.2h  0.94% Wetterbericht
    4037.7h  0.90% Börsenmagazin
    3720.4h  0.83% Quiz
    3471.6h  0.78% Musikmagazin
    3440.0h  0.77% Komödie
    3385.9h  0.76% Wirtschaftsmagazin
    3345.1h  0.75% Wissensmagazin
    3170.5h  0.71% Telenovela
    2961.2h  0.66% Politikmagazin
    2930.8h  0.66% Reportagereihe
