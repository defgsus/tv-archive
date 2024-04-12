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

**102** channels, **806,606.7** hours playtime between **2023-01-17** and **2024-04-13**


### playtime per genre (top 30)

    52513.5h 6.51% Nachrichten
    38726.1h 4.80% Verkaufsshow
    32829.7h 4.07% Krimiserie
    28137.6h 3.49% Werbesendung
    25568.6h 3.17% Dokureihe
    24296.7h 3.01% Dokusoap
    23455.3h 2.91% Regionalmagazin
    20870.2h 2.59% Dokumentation
    20725.5h 2.57% *unknown*
    14807.6h 1.84% Zeichentrickserie
    14634.9h 1.81% Infomercial
    14329.0h 1.78% Animationsserie
    12237.3h 1.52% Comedyserie
    11399.1h 1.41% Morgenmagazin
    11197.8h 1.39% Magazin
    10889.8h 1.35% Religionsmagazin
    10736.6h 1.33% Talkshow
    7942.3h  0.98% E-Sport
    7537.3h  0.93% Programmende
    7463.9h  0.93% Sitcom
    7160.8h  0.89% Wetterbericht
    7110.6h  0.88% Börsenmagazin
    6941.5h  0.86% Quiz
    6909.9h  0.86% Komödie
    5982.3h  0.74% Wissensmagazin
    5879.3h  0.73% Politikmagazin
    5804.6h  0.72% Realityshow
    5786.5h  0.72% Wirtschaftsmagazin
    5767.4h  0.72% Telenovela
    5414.9h  0.67% Musikmagazin
