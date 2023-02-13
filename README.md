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

**96** channels, **51,934.8** hours playtime between **2023-01-17** and **2023-02-14**


### playtime per genre (top 30)

    3602.0h 6.94% Nachrichten
    2686.8h 5.17% Verkaufsshow
    2175.3h 4.19% Krimiserie
    1802.5h 3.47% Dokusoap
    1751.2h 3.37% Werbesendung
    1557.3h 3.00% Dokureihe
    1463.9h 2.82% Regionalmagazin
    1327.5h 2.56% Dokumentation
    1314.2h 2.53% *unknown*
    993.2h  1.91% Zeichentrickserie
    960.8h  1.85% Infomercial
    942.6h  1.81% Animationsserie
    865.5h  1.67% Comedyserie
    721.7h  1.39% Morgenmagazin
    684.4h  1.32% Talkshow
    683.5h  1.32% Programmende
    681.4h  1.31% Religionsmagazin
    586.5h  1.13% Magazin
    545.5h  1.05% E-Sport
    478.1h  0.92% Sitcom
    450.3h  0.87% Wetterbericht
    449.2h  0.86% Börsenmagazin
    432.1h  0.83% Wirtschaftsmagazin
    407.7h  0.79% Wissensmagazin
    397.6h  0.77% Quiz
    384.6h  0.74% Musikmagazin
    378.8h  0.73% Dramaserie
    363.8h  0.70% Gesundheitsmagazin
    363.1h  0.70% Telenovela
    340.4h  0.66% Wirtschaftstalk
