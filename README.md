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

**102** channels, **781,729.3** hours playtime between **2023-01-17** and **2024-03-30**


### playtime per genre (top 30)

    50888.0h 6.51% Nachrichten
    37561.5h 4.80% Verkaufsshow
    31875.0h 4.08% Krimiserie
    27203.8h 3.48% Werbesendung
    24854.0h 3.18% Dokureihe
    23580.1h 3.02% Dokusoap
    22732.9h 2.91% Regionalmagazin
    20212.1h 2.59% Dokumentation
    20061.4h 2.57% *unknown*
    14393.5h 1.84% Zeichentrickserie
    14213.2h 1.82% Infomercial
    13878.6h 1.78% Animationsserie
    11869.2h 1.52% Comedyserie
    11092.5h 1.42% Morgenmagazin
    10732.3h 1.37% Magazin
    10558.5h 1.35% Religionsmagazin
    10427.2h 1.33% Talkshow
    7698.5h  0.98% E-Sport
    7345.4h  0.94% Programmende
    7291.8h  0.93% Sitcom
    6940.5h  0.89% Wetterbericht
    6925.6h  0.89% Börsenmagazin
    6690.1h  0.86% Quiz
    6588.9h  0.84% Komödie
    5826.1h  0.75% Wissensmagazin
    5686.5h  0.73% Politikmagazin
    5629.8h  0.72% Wirtschaftsmagazin
    5618.4h  0.72% Realityshow
    5598.2h  0.72% Telenovela
    5290.7h  0.68% Musikmagazin
