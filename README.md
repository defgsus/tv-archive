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

**102** channels, **829,640.0** hours playtime between **2023-01-17** and **2024-04-28**


### playtime per genre (top 30)

    54064.1h 6.52% Nachrichten
    39766.8h 4.79% Verkaufsshow
    33787.7h 4.07% Krimiserie
    29000.4h 3.50% Werbesendung
    26232.0h 3.16% Dokureihe
    25028.7h 3.02% Dokusoap
    24125.7h 2.91% Regionalmagazin
    21467.7h 2.59% Dokumentation
    21213.9h 2.56% *unknown*
    15240.6h 1.84% Zeichentrickserie
    15073.7h 1.82% Infomercial
    14774.4h 1.78% Animationsserie
    12557.2h 1.51% Comedyserie
    11701.9h 1.41% Morgenmagazin
    11635.1h 1.40% Magazin
    11201.3h 1.35% Religionsmagazin
    11047.3h 1.33% Talkshow
    8215.9h  0.99% E-Sport
    7717.0h  0.93% Programmende
    7632.1h  0.92% Sitcom
    7363.8h  0.89% Wetterbericht
    7297.6h  0.88% Börsenmagazin
    7167.8h  0.86% Quiz
    7085.5h  0.85% Komödie
    6141.9h  0.74% Wissensmagazin
    6072.5h  0.73% Politikmagazin
    6011.9h  0.72% Realityshow
    5932.4h  0.72% Wirtschaftsmagazin
    5930.2h  0.71% Telenovela
    5530.1h  0.67% Musikmagazin
