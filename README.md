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

**97** channels, **464,589.6** hours playtime between **2023-01-17** and **2023-10-02**


### playtime per genre (top 30)

    30620.1h 6.59% Nachrichten
    22109.7h 4.76% Verkaufsshow
    18748.4h 4.04% Krimiserie
    15684.1h 3.38% Werbesendung
    15299.1h 3.29% Dokureihe
    14180.7h 3.05% Dokusoap
    13361.7h 2.88% Regionalmagazin
    11671.1h 2.51% Dokumentation
    11070.8h 2.38% *unknown*
    8726.2h  1.88% Zeichentrickserie
    8475.6h  1.82% Infomercial
    8248.6h  1.78% Animationsserie
    7473.0h  1.61% Comedyserie
    6558.4h  1.41% Morgenmagazin
    6240.2h  1.34% Religionsmagazin
    6159.0h  1.33% Talkshow
    5778.1h  1.24% Magazin
    4897.2h  1.05% Programmende
    4595.3h  0.99% E-Sport
    4383.4h  0.94% Sitcom
    4347.1h  0.94% Wetterbericht
    4187.4h  0.90% Börsenmagazin
    3878.9h  0.83% Quiz
    3593.0h  0.77% Komödie
    3580.9h  0.77% Musikmagazin
    3500.8h  0.75% Wirtschaftsmagazin
    3487.6h  0.75% Wissensmagazin
    3294.0h  0.71% Telenovela
    3105.7h  0.67% Politikmagazin
    3028.4h  0.65% Reportagereihe
