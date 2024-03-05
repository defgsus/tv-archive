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

**99** channels, **741,265.9** hours playtime between **2023-01-17** and **2024-03-06**


### playtime per genre (top 30)

    48224.9h 6.51% Nachrichten
    35591.8h 4.80% Verkaufsshow
    30157.2h 4.07% Krimiserie
    25659.5h 3.46% Werbesendung
    23707.6h 3.20% Dokureihe
    22399.1h 3.02% Dokusoap
    21502.5h 2.90% Regionalmagazin
    19083.3h 2.57% Dokumentation
    19033.9h 2.57% *unknown*
    13720.5h 1.85% Zeichentrickserie
    13478.0h 1.82% Infomercial
    13063.7h 1.76% Animationsserie
    11238.1h 1.52% Comedyserie
    10512.1h 1.42% Morgenmagazin
    10020.3h 1.35% Religionsmagazin
    9984.6h  1.35% Magazin
    9857.0h  1.33% Talkshow
    7321.8h  0.99% E-Sport
    7027.3h  0.95% Programmende
    6987.3h  0.94% Sitcom
    6623.4h  0.89% Börsenmagazin
    6590.4h  0.89% Wetterbericht
    6290.6h  0.85% Komödie
    6259.8h  0.84% Quiz
    5543.1h  0.75% Wissensmagazin
    5396.7h  0.73% Realityshow
    5366.0h  0.72% Wirtschaftsmagazin
    5341.6h  0.72% Politikmagazin
    5285.7h  0.71% Telenovela
    5078.8h  0.69% Musikmagazin
