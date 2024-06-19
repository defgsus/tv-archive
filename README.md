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

**109** channels, **910,734.3** hours playtime between **2023-01-17** and **2024-06-20**


### playtime per genre (top 30)

    59528.7h 6.54% Nachrichten
    42882.6h 4.71% Verkaufsshow
    37111.0h 4.07% Krimiserie
    32193.1h 3.53% Werbesendung
    28645.5h 3.15% Dokureihe
    27540.0h 3.02% Dokusoap
    26504.7h 2.91% Regionalmagazin
    23671.3h 2.60% Dokumentation
    22879.1h 2.51% *unknown*
    16754.4h 1.84% Zeichentrickserie
    16596.2h 1.82% Infomercial
    16256.8h 1.79% Animationsserie
    13622.9h 1.50% Comedyserie
    12988.0h 1.43% Magazin
    12832.0h 1.41% Morgenmagazin
    12332.2h 1.35% Religionsmagazin
    12127.1h 1.33% Talkshow
    9004.2h  0.99% E-Sport
    8518.2h  0.94% Sitcom
    8337.8h  0.92% Programmende
    8133.2h  0.89% Wetterbericht
    7878.1h  0.87% Quiz
    7874.3h  0.86% Komödie
    7818.2h  0.86% Börsenmagazin
    6848.1h  0.75% Politikmagazin
    6762.8h  0.74% Wissensmagazin
    6752.3h  0.74% Realityshow
    6398.2h  0.70% Wirtschaftsmagazin
    6293.1h  0.69% Telenovela
    5979.3h  0.66% Musikmagazin
