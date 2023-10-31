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

**97** channels, **518,289.4** hours playtime between **2023-01-17** and **2023-11-01**


### playtime per genre (top 30)

    34123.2h 6.58% Nachrichten
    24745.6h 4.77% Verkaufsshow
    20839.5h 4.02% Krimiserie
    17557.2h 3.39% Werbesendung
    17063.0h 3.29% Dokureihe
    15787.3h 3.05% Dokusoap
    14961.9h 2.89% Regionalmagazin
    13188.0h 2.54% Dokumentation
    12483.5h 2.41% *unknown*
    9661.6h  1.86% Zeichentrickserie
    9441.5h  1.82% Infomercial
    9267.2h  1.79% Animationsserie
    8199.2h  1.58% Comedyserie
    7354.4h  1.42% Morgenmagazin
    6981.9h  1.35% Religionsmagazin
    6902.8h  1.33% Talkshow
    6519.2h  1.26% Magazin
    5306.5h  1.02% Programmende
    5082.6h  0.98% E-Sport
    4949.0h  0.95% Sitcom
    4800.5h  0.93% Wetterbericht
    4690.6h  0.91% Börsenmagazin
    4343.4h  0.84% Quiz
    4039.8h  0.78% Komödie
    3920.5h  0.76% Wissensmagazin
    3904.6h  0.75% Wirtschaftsmagazin
    3882.8h  0.75% Musikmagazin
    3720.0h  0.72% Telenovela
    3572.8h  0.69% Politikmagazin
    3471.1h  0.67% Realityshow
