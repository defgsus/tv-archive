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

**102** channels, **803,047.8** hours playtime between **2023-01-17** and **2024-04-11**


### playtime per genre (top 30)

    52250.3h 6.51% Nachrichten
    38542.5h 4.80% Verkaufsshow
    32669.1h 4.07% Krimiserie
    28008.2h 3.49% Werbesendung
    25502.2h 3.18% Dokureihe
    24198.3h 3.01% Dokusoap
    23331.7h 2.91% Regionalmagazin
    20791.1h 2.59% Dokumentation
    20657.0h 2.57% *unknown*
    14749.8h 1.84% Zeichentrickserie
    14567.2h 1.81% Infomercial
    14262.6h 1.78% Animationsserie
    12162.5h 1.51% Comedyserie
    11338.3h 1.41% Morgenmagazin
    11135.4h 1.39% Magazin
    10851.2h 1.35% Religionsmagazin
    10688.3h 1.33% Talkshow
    7906.4h  0.98% E-Sport
    7510.2h  0.94% Programmende
    7438.6h  0.93% Sitcom
    7127.9h  0.89% Wetterbericht
    7091.5h  0.88% Börsenmagazin
    6898.6h  0.86% Quiz
    6877.0h  0.86% Komödie
    5962.4h  0.74% Wissensmagazin
    5839.4h  0.73% Politikmagazin
    5773.6h  0.72% Realityshow
    5757.3h  0.72% Wirtschaftsmagazin
    5729.6h  0.71% Telenovela
    5399.0h  0.67% Musikmagazin
