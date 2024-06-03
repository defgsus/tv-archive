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

**108** channels, **885,234.5** hours playtime between **2023-01-17** and **2024-06-04**


### playtime per genre (top 30)

    57781.6h 6.53% Nachrichten
    41921.9h 4.74% Verkaufsshow
    36008.8h 4.07% Krimiserie
    31112.2h 3.51% Werbesendung
    27887.1h 3.15% Dokureihe
    26758.8h 3.02% Dokusoap
    25718.0h 2.91% Regionalmagazin
    22986.5h 2.60% Dokumentation
    22483.5h 2.54% *unknown*
    16276.6h 1.84% Zeichentrickserie
    16113.0h 1.82% Infomercial
    15773.7h 1.78% Animationsserie
    13282.5h 1.50% Comedyserie
    12603.7h 1.42% Magazin
    12445.0h 1.41% Morgenmagazin
    11982.7h 1.35% Religionsmagazin
    11788.4h 1.33% Talkshow
    8776.0h  0.99% E-Sport
    8212.5h  0.93% Sitcom
    8144.7h  0.92% Programmende
    7881.1h  0.89% Wetterbericht
    7732.1h  0.87% Börsenmagazin
    7665.5h  0.87% Quiz
    7653.7h  0.86% Komödie
    6558.6h  0.74% Wissensmagazin
    6546.4h  0.74% Realityshow
    6532.6h  0.74% Politikmagazin
    6258.4h  0.71% Wirtschaftsmagazin
    6202.4h  0.70% Telenovela
    5845.8h  0.66% Musikmagazin
