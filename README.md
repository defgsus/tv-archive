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

**102** channels, **801,214.2** hours playtime between **2023-01-17** and **2024-04-10**


### playtime per genre (top 30)

    52116.0h 6.50% Nachrichten
    38447.8h 4.80% Verkaufsshow
    32608.0h 4.07% Krimiserie
    27941.8h 3.49% Werbesendung
    25447.5h 3.18% Dokureihe
    24128.8h 3.01% Dokusoap
    23264.2h 2.90% Regionalmagazin
    20757.7h 2.59% Dokumentation
    20608.2h 2.57% *unknown*
    14720.9h 1.84% Zeichentrickserie
    14534.4h 1.81% Infomercial
    14227.6h 1.78% Animationsserie
    12127.5h 1.51% Comedyserie
    11307.4h 1.41% Morgenmagazin
    11081.2h 1.38% Magazin
    10829.0h 1.35% Religionsmagazin
    10669.2h 1.33% Talkshow
    7883.9h  0.98% E-Sport
    7496.9h  0.94% Programmende
    7419.8h  0.93% Sitcom
    7111.3h  0.89% Wetterbericht
    7079.1h  0.88% Börsenmagazin
    6876.7h  0.86% Quiz
    6876.6h  0.86% Komödie
    5946.6h  0.74% Wissensmagazin
    5815.4h  0.73% Politikmagazin
    5760.7h  0.72% Realityshow
    5740.6h  0.72% Wirtschaftsmagazin
    5710.3h  0.71% Telenovela
    5389.8h  0.67% Musikmagazin
