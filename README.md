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

**97** channels, **525,509.3** hours playtime between **2023-01-17** and **2023-11-05**


### playtime per genre (top 30)

    34595.7h 6.58% Nachrichten
    25102.5h 4.78% Verkaufsshow
    21125.1h 4.02% Krimiserie
    17801.2h 3.39% Werbesendung
    17268.0h 3.29% Dokureihe
    15970.7h 3.04% Dokusoap
    15154.9h 2.88% Regionalmagazin
    13404.3h 2.55% Dokumentation
    12682.5h 2.41% *unknown*
    9785.2h  1.86% Zeichentrickserie
    9569.5h  1.82% Infomercial
    9398.2h  1.79% Animationsserie
    8298.9h  1.58% Comedyserie
    7466.9h  1.42% Morgenmagazin
    7076.9h  1.35% Religionsmagazin
    6998.9h  1.33% Talkshow
    6639.4h  1.26% Magazin
    5358.5h  1.02% Programmende
    5164.8h  0.98% E-Sport
    5019.8h  0.96% Sitcom
    4862.9h  0.93% Wetterbericht
    4751.0h  0.90% Börsenmagazin
    4392.2h  0.84% Quiz
    4138.6h  0.79% Komödie
    3971.0h  0.76% Wissensmagazin
    3956.0h  0.75% Wirtschaftsmagazin
    3920.8h  0.75% Musikmagazin
    3779.0h  0.72% Telenovela
    3621.8h  0.69% Politikmagazin
    3548.7h  0.68% Realityshow
