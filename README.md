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

**97** channels, **459,176.5** hours playtime between **2023-01-17** and **2023-09-29**


### playtime per genre (top 30)

    30324.2h 6.60% Nachrichten
    21840.1h 4.76% Verkaufsshow
    18547.0h 4.04% Krimiserie
    15493.6h 3.37% Werbesendung
    15134.4h 3.30% Dokureihe
    14010.8h 3.05% Dokusoap
    13250.2h 2.89% Regionalmagazin
    11544.0h 2.51% Dokumentation
    10934.0h 2.38% *unknown*
    8640.8h  1.88% Zeichentrickserie
    8377.8h  1.82% Infomercial
    8155.1h  1.78% Animationsserie
    7413.4h  1.61% Comedyserie
    6512.1h  1.42% Morgenmagazin
    6148.8h  1.34% Religionsmagazin
    6082.3h  1.32% Talkshow
    5725.3h  1.25% Magazin
    4851.1h  1.06% Programmende
    4529.4h  0.99% E-Sport
    4342.0h  0.95% Sitcom
    4311.3h  0.94% Wetterbericht
    4138.9h  0.90% Börsenmagazin
    3847.1h  0.84% Quiz
    3546.1h  0.77% Musikmagazin
    3536.7h  0.77% Komödie
    3476.7h  0.76% Wirtschaftsmagazin
    3449.8h  0.75% Wissensmagazin
    3270.6h  0.71% Telenovela
    3074.9h  0.67% Politikmagazin
    3002.3h  0.65% Reportagereihe
