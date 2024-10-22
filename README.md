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

**109** channels, **1,103,398.9** hours playtime between **2023-01-17** and **2024-10-23**


### playtime per genre (top 30)

    71840.2h 6.51% Nachrichten
    50840.0h 4.61% Verkaufsshow
    45832.7h 4.15% Krimiserie
    40382.0h 3.66% Werbesendung
    34520.8h 3.13% Dokureihe
    33007.8h 2.99% Dokusoap
    32261.0h 2.92% Regionalmagazin
    28918.0h 2.62% Dokumentation
    26228.0h 2.38% *unknown*
    20581.8h 1.87% Zeichentrickserie
    20302.9h 1.84% Infomercial
    19742.7h 1.79% Animationsserie
    15950.0h 1.45% Comedyserie
    15439.9h 1.40% Morgenmagazin
    14880.9h 1.35% Religionsmagazin
    14586.1h 1.32% Talkshow
    14026.2h 1.27% Magazin
    10911.3h 0.99% E-Sport
    10623.3h 0.96% Sitcom
    9996.1h  0.91% Wetterbericht
    9803.5h  0.89% Programmende
    9677.1h  0.88% Quiz
    9670.0h  0.88% Komödie
    8427.6h  0.76% Börsenmagazin
    8394.2h  0.76% Realityshow
    8343.7h  0.76% Politikmagazin
    8291.0h  0.75% Wissensmagazin
    7424.9h  0.67% Wirtschaftsmagazin
    7274.5h  0.66% Telenovela
    7211.2h  0.65% Dramaserie
