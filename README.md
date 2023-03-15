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

**96** channels, **106,490.7** hours playtime between **2023-01-17** and **2023-03-16**


### playtime per genre (top 30)

    7512.2h 7.05% Nachrichten
    5350.8h 5.02% Verkaufsshow
    4480.6h 4.21% Krimiserie
    3609.2h 3.39% Werbesendung
    3412.3h 3.20% Dokusoap
    3232.0h 3.04% Dokureihe
    3144.0h 2.95% Regionalmagazin
    2621.7h 2.46% Dokumentation
    2513.0h 2.36% *unknown*
    2041.1h 1.92% Animationsserie
    1952.9h 1.83% Infomercial
    1920.8h 1.80% Zeichentrickserie
    1746.2h 1.64% Comedyserie
    1521.2h 1.43% Morgenmagazin
    1453.1h 1.36% Programmende
    1413.6h 1.33% Talkshow
    1392.4h 1.31% Religionsmagazin
    1100.2h 1.03% Magazin
    1098.6h 1.03% E-Sport
    1021.1h 0.96% Sitcom
    997.5h  0.94% Börsenmagazin
    945.1h  0.89% Wetterbericht
    870.6h  0.82% Wirtschaftsmagazin
    838.4h  0.79% Wissensmagazin
    807.9h  0.76% Quiz
    786.1h  0.74% Musikmagazin
    764.7h  0.72% Dramaserie
    748.8h  0.70% Telenovela
    744.6h  0.70% Gesundheitsmagazin
    692.6h  0.65% Sportmagazin
