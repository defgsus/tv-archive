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

**102** channels, **797,747.2** hours playtime between **2023-01-17** and **2024-04-08**


### playtime per genre (top 30)

    51852.0h 6.50% Nachrichten
    38284.7h 4.80% Verkaufsshow
    32434.7h 4.07% Krimiserie
    27813.8h 3.49% Werbesendung
    25364.0h 3.18% Dokureihe
    24014.2h 3.01% Dokusoap
    23136.8h 2.90% Regionalmagazin
    20680.2h 2.59% Dokumentation
    20513.7h 2.57% *unknown*
    14659.0h 1.84% Zeichentrickserie
    14470.5h 1.81% Infomercial
    14161.8h 1.78% Animationsserie
    12062.7h 1.51% Comedyserie
    11245.5h 1.41% Morgenmagazin
    11031.1h 1.38% Magazin
    10786.4h 1.35% Religionsmagazin
    10624.9h 1.33% Talkshow
    7855.4h  0.98% E-Sport
    7470.1h  0.94% Programmende
    7390.6h  0.93% Sitcom
    7079.1h  0.89% Wetterbericht
    7038.1h  0.88% Börsenmagazin
    6868.6h  0.86% Komödie
    6828.6h  0.86% Quiz
    5933.1h  0.74% Wissensmagazin
    5775.6h  0.72% Politikmagazin
    5727.4h  0.72% Realityshow
    5717.8h  0.72% Wirtschaftsmagazin
    5673.9h  0.71% Telenovela
    5374.9h  0.67% Musikmagazin
