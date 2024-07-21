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

**109** channels, **959,638.2** hours playtime between **2023-01-17** and **2024-07-22**


### playtime per genre (top 30)

    62473.6h 6.51% Nachrichten
    44823.5h 4.67% Verkaufsshow
    39295.9h 4.09% Krimiserie
    34273.0h 3.57% Werbesendung
    30203.6h 3.15% Dokureihe
    29049.2h 3.03% Dokusoap
    27895.0h 2.91% Regionalmagazin
    24926.8h 2.60% Dokumentation
    23918.9h 2.49% *unknown*
    17747.9h 1.85% Zeichentrickserie
    17540.7h 1.83% Infomercial
    17160.1h 1.79% Animationsserie
    14257.9h 1.49% Comedyserie
    13487.5h 1.41% Morgenmagazin
    13405.0h 1.40% Magazin
    13030.5h 1.36% Religionsmagazin
    12690.3h 1.32% Talkshow
    9503.0h  0.99% E-Sport
    9050.4h  0.94% Sitcom
    8710.9h  0.91% Programmende
    8603.2h  0.90% Wetterbericht
    8386.8h  0.87% Komödie
    8271.2h  0.86% Quiz
    7966.4h  0.83% Börsenmagazin
    7218.1h  0.75% Politikmagazin
    7137.7h  0.74% Wissensmagazin
    7119.0h  0.74% Realityshow
    6639.8h  0.69% Wirtschaftsmagazin
    6431.0h  0.67% Telenovela
    6249.2h  0.65% Dramaserie
