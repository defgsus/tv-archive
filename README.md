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

**96** channels, **131,844.8** hours playtime between **2023-01-17** and **2023-03-31**


### playtime per genre (top 30)

    9270.0h 7.03% Nachrichten
    6586.6h 5.00% Verkaufsshow
    5512.3h 4.18% Krimiserie
    4458.9h 3.38% Werbesendung
    4103.1h 3.11% Dokusoap
    4097.6h 3.11% Dokureihe
    3900.8h 2.96% Regionalmagazin
    3273.3h 2.48% Dokumentation
    3014.4h 2.29% *unknown*
    2502.4h 1.90% Animationsserie
    2429.1h 1.84% Infomercial
    2414.1h 1.83% Zeichentrickserie
    2173.3h 1.65% Comedyserie
    1894.2h 1.44% Morgenmagazin
    1836.5h 1.39% Programmende
    1754.6h 1.33% Talkshow
    1708.3h 1.30% Religionsmagazin
    1390.0h 1.05% Magazin
    1366.2h 1.04% E-Sport
    1264.2h 0.96% Sitcom
    1239.6h 0.94% Börsenmagazin
    1185.1h 0.90% Wetterbericht
    1082.7h 0.82% Wirtschaftsmagazin
    1034.7h 0.78% Wissensmagazin
    1010.0h 0.77% Quiz
    993.7h  0.75% Musikmagazin
    950.5h  0.72% Dramaserie
    934.0h  0.71% Telenovela
    908.9h  0.69% Gesundheitsmagazin
    898.0h  0.68% Sportmagazin
