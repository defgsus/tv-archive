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

**99** channels, **705,705.0** hours playtime between **2023-01-17** and **2024-02-15**


### playtime per genre (top 30)

    45982.0h 6.52% Nachrichten
    33878.0h 4.80% Verkaufsshow
    28556.0h 4.05% Krimiserie
    24241.4h 3.44% Werbesendung
    22699.4h 3.22% Dokureihe
    21253.4h 3.01% Dokusoap
    20428.1h 2.89% Regionalmagazin
    18181.4h 2.58% Dokumentation
    17840.8h 2.53% *unknown*
    13086.7h 1.85% Zeichentrickserie
    12826.4h 1.82% Infomercial
    12408.4h 1.76% Animationsserie
    10685.4h 1.51% Comedyserie
    10000.4h 1.42% Morgenmagazin
    9539.3h  1.35% Religionsmagazin
    9425.1h  1.34% Magazin
    9347.2h  1.32% Talkshow
    6950.1h  0.98% E-Sport
    6752.2h  0.96% Programmende
    6718.6h  0.95% Sitcom
    6293.5h  0.89% Börsenmagazin
    6286.8h  0.89% Wetterbericht
    5996.1h  0.85% Komödie
    5882.2h  0.83% Quiz
    5297.1h  0.75% Wissensmagazin
    5186.3h  0.73% Realityshow
    5138.9h  0.73% Wirtschaftsmagazin
    5054.2h  0.72% Politikmagazin
    5027.6h  0.71% Telenovela
    4901.4h  0.69% Musikmagazin
