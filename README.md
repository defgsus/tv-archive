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

**96** channels, **183,041.2** hours playtime between **2023-01-17** and **2023-04-28**


### playtime per genre (top 30)

    12482.0h 6.82% Nachrichten
    9018.4h  4.93% Verkaufsshow
    7509.8h  4.10% Krimiserie
    6097.2h  3.33% Werbesendung
    5886.2h  3.22% Dokureihe
    5446.5h  2.98% Dokusoap
    5316.8h  2.90% Regionalmagazin
    4583.7h  2.50% Dokumentation
    4428.5h  2.42% *unknown*
    3377.7h  1.85% Zeichentrickserie
    3352.7h  1.83% Infomercial
    3351.2h  1.83% Animationsserie
    3058.8h  1.67% Comedyserie
    2559.6h  1.40% Morgenmagazin
    2533.4h  1.38% Programmende
    2390.8h  1.31% Talkshow
    2378.1h  1.30% Religionsmagazin
    2021.5h  1.10% Magazin
    1852.1h  1.01% E-Sport
    1728.7h  0.94% Sitcom
    1661.8h  0.91% Börsenmagazin
    1656.7h  0.91% Wetterbericht
    1463.1h  0.80% Wirtschaftsmagazin
    1438.8h  0.79% Wissensmagazin
    1410.9h  0.77% Quiz
    1402.1h  0.77% Musikmagazin
    1295.2h  0.71% Telenovela
    1272.0h  0.69% Gesundheitsmagazin
    1261.8h  0.69% Sportmagazin
    1248.5h  0.68% Dramaserie
