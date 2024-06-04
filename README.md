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

**108** channels, **887,164.4** hours playtime between **2023-01-17** and **2024-06-05**


### playtime per genre (top 30)

    57972.8h 6.53% Nachrichten
    41980.5h 4.73% Verkaufsshow
    36111.7h 4.07% Krimiserie
    31202.7h 3.52% Werbesendung
    27939.9h 3.15% Dokureihe
    26819.1h 3.02% Dokusoap
    25786.5h 2.91% Regionalmagazin
    23049.7h 2.60% Dokumentation
    22431.7h 2.53% *unknown*
    16312.6h 1.84% Zeichentrickserie
    16147.3h 1.82% Infomercial
    15812.9h 1.78% Animationsserie
    13312.6h 1.50% Comedyserie
    12643.0h 1.43% Magazin
    12482.9h 1.41% Morgenmagazin
    12014.5h 1.35% Religionsmagazin
    11810.5h 1.33% Talkshow
    8784.3h  0.99% E-Sport
    8233.0h  0.93% Sitcom
    8158.6h  0.92% Programmende
    7902.5h  0.89% Wetterbericht
    7741.8h  0.87% Börsenmagazin
    7684.5h  0.87% Quiz
    7657.4h  0.86% Komödie
    6572.2h  0.74% Wissensmagazin
    6566.5h  0.74% Politikmagazin
    6552.6h  0.74% Realityshow
    6273.3h  0.71% Wirtschaftsmagazin
    6213.1h  0.70% Telenovela
    5858.9h  0.66% Musikmagazin
