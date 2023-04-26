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

**96** channels, **181,191.5** hours playtime between **2023-01-17** and **2023-04-27**


### playtime per genre (top 30)

    12347.1h 6.81% Nachrichten
    8926.6h  4.93% Verkaufsshow
    7430.3h  4.10% Krimiserie
    6042.8h  3.34% Werbesendung
    5835.2h  3.22% Dokureihe
    5377.7h  2.97% Dokusoap
    5249.1h  2.90% Regionalmagazin
    4548.8h  2.51% Dokumentation
    4357.9h  2.41% *unknown*
    3345.1h  1.85% Zeichentrickserie
    3322.2h  1.83% Animationsserie
    3315.8h  1.83% Infomercial
    3013.0h  1.66% Comedyserie
    2525.3h  1.39% Morgenmagazin
    2498.0h  1.38% Programmende
    2371.7h  1.31% Talkshow
    2360.1h  1.30% Religionsmagazin
    1991.4h  1.10% Magazin
    1844.7h  1.02% E-Sport
    1712.1h  0.94% Sitcom
    1649.4h  0.91% Börsenmagazin
    1638.2h  0.90% Wetterbericht
    1446.5h  0.80% Wirtschaftsmagazin
    1424.8h  0.79% Wissensmagazin
    1395.3h  0.77% Quiz
    1386.0h  0.76% Musikmagazin
    1275.0h  0.70% Telenovela
    1259.4h  0.70% Gesundheitsmagazin
    1254.6h  0.69% Sportmagazin
    1227.9h  0.68% Dramaserie
