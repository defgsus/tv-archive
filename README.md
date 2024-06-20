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

**109** channels, **912,555.8** hours playtime between **2023-01-17** and **2024-06-21**


### playtime per genre (top 30)

    59655.7h 6.54% Nachrichten
    42952.1h 4.71% Verkaufsshow
    37209.6h 4.08% Krimiserie
    32267.6h 3.54% Werbesendung
    28717.9h 3.15% Dokureihe
    27588.2h 3.02% Dokusoap
    26570.5h 2.91% Regionalmagazin
    23704.9h 2.60% Dokumentation
    22910.5h 2.51% *unknown*
    16786.5h 1.84% Zeichentrickserie
    16630.7h 1.82% Infomercial
    16296.1h 1.79% Animationsserie
    13655.8h 1.50% Comedyserie
    13016.8h 1.43% Magazin
    12868.0h 1.41% Morgenmagazin
    12354.4h 1.35% Religionsmagazin
    12145.6h 1.33% Talkshow
    9028.0h  0.99% E-Sport
    8537.2h  0.94% Sitcom
    8351.8h  0.92% Programmende
    8150.1h  0.89% Wetterbericht
    7894.6h  0.87% Quiz
    7887.3h  0.86% Komödie
    7827.2h  0.86% Börsenmagazin
    6877.6h  0.75% Politikmagazin
    6774.9h  0.74% Realityshow
    6773.5h  0.74% Wissensmagazin
    6408.5h  0.70% Wirtschaftsmagazin
    6299.8h  0.69% Telenovela
    5989.1h  0.66% Musikmagazin
