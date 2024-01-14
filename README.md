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

**99** channels, **650,639.0** hours playtime between **2023-01-17** and **2024-01-15**


### playtime per genre (top 30)

    42419.6h 6.52% Nachrichten
    31076.3h 4.78% Verkaufsshow
    26081.5h 4.01% Krimiserie
    22168.2h 3.41% Werbesendung
    21160.2h 3.25% Dokureihe
    19438.2h 2.99% Dokusoap
    18688.5h 2.87% Regionalmagazin
    16910.8h 2.60% Dokumentation
    16225.1h 2.49% *unknown*
    12017.9h 1.85% Zeichentrickserie
    11804.7h 1.81% Infomercial
    11440.3h 1.76% Animationsserie
    9855.4h  1.51% Comedyserie
    9183.4h  1.41% Morgenmagazin
    8808.6h  1.35% Religionsmagazin
    8596.2h  1.32% Talkshow
    8591.1h  1.32% Magazin
    6392.2h  0.98% E-Sport
    6315.9h  0.97% Programmende
    6276.2h  0.96% Sitcom
    5891.5h  0.91% Wetterbericht
    5782.9h  0.89% Börsenmagazin
    5535.1h  0.85% Komödie
    5357.4h  0.82% Quiz
    4902.8h  0.75% Wissensmagazin
    4764.9h  0.73% Wirtschaftsmagazin
    4724.1h  0.73% Realityshow
    4625.6h  0.71% Musikmagazin
    4618.8h  0.71% Telenovela
    4566.0h  0.70% Politikmagazin
