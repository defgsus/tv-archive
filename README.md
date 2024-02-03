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

**99** channels, **686,153.8** hours playtime between **2023-01-17** and **2024-02-04**


### playtime per genre (top 30)

    44732.9h 6.52% Nachrichten
    32875.4h 4.79% Verkaufsshow
    27677.7h 4.03% Krimiserie
    23523.1h 3.43% Werbesendung
    22184.7h 3.23% Dokureihe
    20600.9h 3.00% Dokusoap
    19830.7h 2.89% Regionalmagazin
    17698.7h 2.58% Dokumentation
    17289.7h 2.52% *unknown*
    12722.7h 1.85% Zeichentrickserie
    12469.9h 1.82% Infomercial
    12063.3h 1.76% Animationsserie
    10387.0h 1.51% Comedyserie
    9708.9h  1.41% Morgenmagazin
    9262.0h  1.35% Religionsmagazin
    9117.2h  1.33% Magazin
    9072.8h  1.32% Talkshow
    6742.4h  0.98% E-Sport
    6599.0h  0.96% Programmende
    6554.8h  0.96% Sitcom
    6142.5h  0.90% Wetterbericht
    6108.0h  0.89% Börsenmagazin
    5826.1h  0.85% Komödie
    5708.6h  0.83% Quiz
    5161.8h  0.75% Wissensmagazin
    5039.5h  0.73% Realityshow
    5001.2h  0.73% Wirtschaftsmagazin
    4887.4h  0.71% Politikmagazin
    4886.9h  0.71% Telenovela
    4801.4h  0.70% Musikmagazin
