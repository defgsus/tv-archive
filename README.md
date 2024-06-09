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

**108** channels, **894,428.9** hours playtime between **2023-01-17** and **2024-06-10**


### playtime per genre (top 30)

    58432.6h 6.53% Nachrichten
    42271.8h 4.73% Verkaufsshow
    36381.7h 4.07% Krimiserie
    31512.5h 3.52% Werbesendung
    28178.1h 3.15% Dokureihe
    27037.9h 3.02% Dokusoap
    25972.6h 2.90% Regionalmagazin
    23238.3h 2.60% Dokumentation
    22579.8h 2.52% *unknown*
    16450.8h 1.84% Zeichentrickserie
    16290.0h 1.82% Infomercial
    15941.4h 1.78% Animationsserie
    13397.0h 1.50% Comedyserie
    12775.2h 1.43% Magazin
    12570.4h 1.41% Morgenmagazin
    12116.8h 1.35% Religionsmagazin
    11923.1h 1.33% Talkshow
    8856.7h  0.99% E-Sport
    8312.2h  0.93% Sitcom
    8212.7h  0.92% Programmende
    7971.4h  0.89% Wetterbericht
    7758.5h  0.87% Börsenmagazin
    7742.0h  0.87% Quiz
    7740.6h  0.87% Komödie
    6634.4h  0.74% Wissensmagazin
    6629.4h  0.74% Politikmagazin
    6607.2h  0.74% Realityshow
    6312.6h  0.71% Wirtschaftsmagazin
    6234.5h  0.70% Telenovela
    5903.1h  0.66% Musikmagazin
