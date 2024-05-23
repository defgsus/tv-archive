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

**108** channels, **868,901.7** hours playtime between **2023-01-17** and **2024-05-24**


### playtime per genre (top 30)

    56784.1h 6.54% Nachrichten
    41306.9h 4.75% Verkaufsshow
    35388.0h 4.07% Krimiserie
    30450.6h 3.50% Werbesendung
    27362.2h 3.15% Dokureihe
    26259.1h 3.02% Dokusoap
    25275.9h 2.91% Regionalmagazin
    22537.0h 2.59% Dokumentation
    22051.8h 2.54% *unknown*
    15968.0h 1.84% Zeichentrickserie
    15797.5h 1.82% Infomercial
    15473.4h 1.78% Animationsserie
    13068.3h 1.50% Comedyserie
    12348.9h 1.42% Magazin
    12243.5h 1.41% Morgenmagazin
    11743.4h 1.35% Religionsmagazin
    11571.1h 1.33% Talkshow
    8605.8h  0.99% E-Sport
    8031.2h  0.92% Sitcom
    8020.2h  0.92% Programmende
    7731.1h  0.89% Wetterbericht
    7621.6h  0.88% Börsenmagazin
    7520.7h  0.87% Quiz
    7482.9h  0.86% Komödie
    6427.3h  0.74% Realityshow
    6423.7h  0.74% Wissensmagazin
    6393.7h  0.74% Politikmagazin
    6180.7h  0.71% Wirtschaftsmagazin
    6144.0h  0.71% Telenovela
    5748.8h  0.66% Musikmagazin
