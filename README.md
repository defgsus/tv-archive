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

**108** channels, **874,389.6** hours playtime between **2023-01-17** and **2024-05-28**


### playtime per genre (top 30)

    57109.7h 6.53% Nachrichten
    41514.3h 4.75% Verkaufsshow
    35572.6h 4.07% Krimiserie
    30671.6h 3.51% Werbesendung
    27558.6h 3.15% Dokureihe
    26431.6h 3.02% Dokusoap
    25398.4h 2.90% Regionalmagazin
    22697.5h 2.60% Dokumentation
    22164.2h 2.53% *unknown*
    16071.6h 1.84% Zeichentrickserie
    15904.5h 1.82% Infomercial
    15579.5h 1.78% Animationsserie
    13139.8h 1.50% Comedyserie
    12417.0h 1.42% Magazin
    12293.4h 1.41% Morgenmagazin
    11829.1h 1.35% Religionsmagazin
    11643.9h 1.33% Talkshow
    8661.4h  0.99% E-Sport
    8082.4h  0.92% Sitcom
    8058.8h  0.92% Programmende
    7776.0h  0.89% Wetterbericht
    7648.2h  0.87% Börsenmagazin
    7568.3h  0.87% Quiz
    7549.2h  0.86% Komödie
    6463.5h  0.74% Wissensmagazin
    6460.4h  0.74% Realityshow
    6420.1h  0.73% Politikmagazin
    6200.3h  0.71% Wirtschaftsmagazin
    6157.6h  0.70% Telenovela
    5782.8h  0.66% Musikmagazin
