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

**102** channels, **836,435.7** hours playtime between **2023-01-17** and **2024-05-02**


### playtime per genre (top 30)

    54535.0h 6.52% Nachrichten
    40022.6h 4.78% Verkaufsshow
    34032.3h 4.07% Krimiserie
    29242.6h 3.50% Werbesendung
    26454.0h 3.16% Dokureihe
    25244.8h 3.02% Dokusoap
    24314.4h 2.91% Regionalmagazin
    21691.2h 2.59% Dokumentation
    21354.4h 2.55% *unknown*
    15375.6h 1.84% Zeichentrickserie
    15194.3h 1.82% Infomercial
    14888.8h 1.78% Animationsserie
    12648.1h 1.51% Comedyserie
    11778.4h 1.41% Morgenmagazin
    11774.1h 1.41% Magazin
    11294.9h 1.35% Religionsmagazin
    11130.6h 1.33% Talkshow
    8287.8h  0.99% E-Sport
    7773.1h  0.93% Programmende
    7697.7h  0.92% Sitcom
    7426.6h  0.89% Wetterbericht
    7357.1h  0.88% Börsenmagazin
    7223.1h  0.86% Quiz
    7150.3h  0.85% Komödie
    6186.7h  0.74% Wissensmagazin
    6134.2h  0.73% Politikmagazin
    6111.5h  0.73% Realityshow
    5977.6h  0.71% Wirtschaftsmagazin
    5967.1h  0.71% Telenovela
    5569.1h  0.67% Musikmagazin
