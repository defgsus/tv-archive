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

**101** channels, **772,905.9** hours playtime between **2023-01-17** and **2024-03-24**


### playtime per genre (top 30)

    50319.2h 6.51% Nachrichten
    37145.4h 4.81% Verkaufsshow
    31528.9h 4.08% Krimiserie
    26862.7h 3.48% Werbesendung
    24559.0h 3.18% Dokureihe
    23340.0h 3.02% Dokusoap
    22469.1h 2.91% Regionalmagazin
    19935.5h 2.58% Dokumentation
    19830.1h 2.57% *unknown*
    14242.0h 1.84% Zeichentrickserie
    14064.5h 1.82% Infomercial
    13708.1h 1.77% Animationsserie
    11728.0h 1.52% Comedyserie
    10973.4h 1.42% Morgenmagazin
    10555.7h 1.37% Magazin
    10437.8h 1.35% Religionsmagazin
    10316.4h 1.33% Talkshow
    7607.1h  0.98% E-Sport
    7274.9h  0.94% Programmende
    7223.6h  0.93% Sitcom
    6865.8h  0.89% Börsenmagazin
    6862.8h  0.89% Wetterbericht
    6603.3h  0.85% Quiz
    6499.0h  0.84% Komödie
    5770.1h  0.75% Wissensmagazin
    5621.7h  0.73% Politikmagazin
    5580.6h  0.72% Realityshow
    5574.7h  0.72% Wirtschaftsmagazin
    5536.2h  0.72% Telenovela
    5247.3h  0.68% Musikmagazin
