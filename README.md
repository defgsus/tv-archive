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

**102** channels, **812,366.2** hours playtime between **2023-01-17** and **2024-04-17**


### playtime per genre (top 30)

    52882.2h 6.51% Nachrichten
    38992.2h 4.80% Verkaufsshow
    33076.7h 4.07% Krimiserie
    28348.0h 3.49% Werbesendung
    25742.1h 3.17% Dokureihe
    24490.7h 3.01% Dokusoap
    23615.9h 2.91% Regionalmagazin
    21037.0h 2.59% Dokumentation
    20829.2h 2.56% *unknown*
    14913.4h 1.84% Zeichentrickserie
    14746.7h 1.82% Infomercial
    14442.5h 1.78% Animationsserie
    12319.7h 1.52% Comedyserie
    11469.4h 1.41% Morgenmagazin
    11290.5h 1.39% Magazin
    10963.7h 1.35% Religionsmagazin
    10814.1h 1.33% Talkshow
    8016.0h  0.99% E-Sport
    7579.3h  0.93% Programmende
    7503.0h  0.92% Sitcom
    7208.0h  0.89% Wetterbericht
    7167.1h  0.88% Börsenmagazin
    7001.5h  0.86% Quiz
    6945.3h  0.85% Komödie
    6023.7h  0.74% Wissensmagazin
    5926.8h  0.73% Politikmagazin
    5848.7h  0.72% Realityshow
    5819.5h  0.72% Wirtschaftsmagazin
    5806.0h  0.71% Telenovela
    5441.7h  0.67% Musikmagazin
