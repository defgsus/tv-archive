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

**99** channels, **735,950.5** hours playtime between **2023-01-17** and **2024-03-03**


### playtime per genre (top 30)

    47898.6h 6.51% Nachrichten
    35322.0h 4.80% Verkaufsshow
    29921.0h 4.07% Krimiserie
    25456.7h 3.46% Werbesendung
    23538.3h 3.20% Dokureihe
    22229.7h 3.02% Dokusoap
    21338.2h 2.90% Regionalmagazin
    18954.3h 2.58% Dokumentation
    18873.3h 2.56% *unknown*
    13623.7h 1.85% Zeichentrickserie
    13383.3h 1.82% Infomercial
    12965.4h 1.76% Animationsserie
    11146.1h 1.51% Comedyserie
    10436.4h 1.42% Morgenmagazin
    9941.8h  1.35% Religionsmagazin
    9908.1h  1.35% Magazin
    9774.0h  1.33% Talkshow
    7270.4h  0.99% E-Sport
    6986.2h  0.95% Programmende
    6941.9h  0.94% Sitcom
    6566.3h  0.89% Börsenmagazin
    6543.6h  0.89% Wetterbericht
    6236.6h  0.85% Komödie
    6202.3h  0.84% Quiz
    5503.6h  0.75% Wissensmagazin
    5355.9h  0.73% Realityshow
    5331.7h  0.72% Wirtschaftsmagazin
    5297.2h  0.72% Politikmagazin
    5247.4h  0.71% Telenovela
    5051.8h  0.69% Musikmagazin
