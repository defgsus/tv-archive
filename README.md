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

**109** channels, **999,705.3** hours playtime between **2023-01-17** and **2024-08-17**


### playtime per genre (top 30)

    65054.6h 6.51% Nachrichten
    46573.1h 4.66% Verkaufsshow
    41028.0h 4.10% Krimiserie
    35962.7h 3.60% Werbesendung
    31406.8h 3.14% Dokureihe
    30213.0h 3.02% Dokusoap
    29141.7h 2.92% Regionalmagazin
    26048.7h 2.61% Dokumentation
    24469.9h 2.45% *unknown*
    18529.0h 1.85% Zeichentrickserie
    18302.0h 1.83% Infomercial
    17893.7h 1.79% Animationsserie
    14725.8h 1.47% Comedyserie
    14032.6h 1.40% Morgenmagazin
    13587.1h 1.36% Religionsmagazin
    13503.1h 1.35% Magazin
    13115.9h 1.31% Talkshow
    9896.1h  0.99% E-Sport
    9509.3h  0.95% Sitcom
    9015.1h  0.90% Programmende
    9011.0h  0.90% Wetterbericht
    8741.3h  0.87% Komödie
    8613.1h  0.86% Quiz
    8110.9h  0.81% Börsenmagazin
    7484.9h  0.75% Politikmagazin
    7437.9h  0.74% Wissensmagazin
    7413.6h  0.74% Realityshow
    6847.7h  0.68% Wirtschaftsmagazin
    6581.6h  0.66% Telenovela
    6519.7h  0.65% Dramaserie
