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

**108** channels, **868,902.8** hours playtime between **2023-01-17** and **2024-05-25**


### playtime per genre (top 30)

    56770.7h 6.53% Nachrichten
    41305.2h 4.75% Verkaufsshow
    35369.5h 4.07% Krimiserie
    30453.5h 3.50% Werbesendung
    27340.9h 3.15% Dokureihe
    26278.0h 3.02% Dokusoap
    25275.0h 2.91% Regionalmagazin
    22547.9h 2.59% Dokumentation
    22068.2h 2.54% *unknown*
    15972.2h 1.84% Zeichentrickserie
    15797.7h 1.82% Infomercial
    15472.2h 1.78% Animationsserie
    13074.9h 1.50% Comedyserie
    12342.5h 1.42% Magazin
    12243.5h 1.41% Morgenmagazin
    11746.9h 1.35% Religionsmagazin
    11569.6h 1.33% Talkshow
    8605.9h  0.99% E-Sport
    8031.2h  0.92% Sitcom
    8020.4h  0.92% Programmende
    7731.0h  0.89% Wetterbericht
    7622.1h  0.88% Börsenmagazin
    7525.4h  0.87% Quiz
    7499.0h  0.86% Komödie
    6421.5h  0.74% Realityshow
    6418.9h  0.74% Wissensmagazin
    6375.9h  0.73% Politikmagazin
    6180.1h  0.71% Wirtschaftsmagazin
    6146.6h  0.71% Telenovela
    5750.8h  0.66% Musikmagazin
