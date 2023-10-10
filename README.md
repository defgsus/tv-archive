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

**97** channels, **480,666.8** hours playtime between **2023-01-17** and **2023-10-11**


### playtime per genre (top 30)

    31661.8h 6.59% Nachrichten
    22914.2h 4.77% Verkaufsshow
    19353.0h 4.03% Krimiserie
    16231.6h 3.38% Werbesendung
    15856.3h 3.30% Dokureihe
    14698.8h 3.06% Dokusoap
    13832.5h 2.88% Regionalmagazin
    12142.9h 2.53% Dokumentation
    11486.6h 2.39% *unknown*
    9023.1h  1.88% Zeichentrickserie
    8755.2h  1.82% Infomercial
    8553.0h  1.78% Animationsserie
    7698.4h  1.60% Comedyserie
    6787.0h  1.41% Morgenmagazin
    6455.6h  1.34% Religionsmagazin
    6383.5h  1.33% Talkshow
    5982.0h  1.24% Magazin
    5014.9h  1.04% Programmende
    4743.0h  0.99% E-Sport
    4561.8h  0.95% Sitcom
    4489.5h  0.93% Wetterbericht
    4353.7h  0.91% Börsenmagazin
    4034.9h  0.84% Quiz
    3735.9h  0.78% Komödie
    3672.8h  0.76% Musikmagazin
    3620.1h  0.75% Wirtschaftsmagazin
    3616.2h  0.75% Wissensmagazin
    3419.4h  0.71% Telenovela
    3252.2h  0.68% Politikmagazin
    3122.5h  0.65% Reportagereihe
