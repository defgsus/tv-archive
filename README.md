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

**96** channels, **131,847.4** hours playtime between **2023-01-17** and **2023-03-31**


### playtime per genre (top 30)

    9268.9h 7.03% Nachrichten
    6586.7h 5.00% Verkaufsshow
    5512.2h 4.18% Krimiserie
    4460.2h 3.38% Werbesendung
    4104.3h 3.11% Dokusoap
    4097.5h 3.11% Dokureihe
    3900.8h 2.96% Regionalmagazin
    3273.2h 2.48% Dokumentation
    3009.5h 2.28% *unknown*
    2502.4h 1.90% Animationsserie
    2429.1h 1.84% Infomercial
    2414.1h 1.83% Zeichentrickserie
    2174.3h 1.65% Comedyserie
    1894.2h 1.44% Morgenmagazin
    1836.6h 1.39% Programmende
    1754.0h 1.33% Talkshow
    1708.3h 1.30% Religionsmagazin
    1390.0h 1.05% Magazin
    1368.9h 1.04% E-Sport
    1264.4h 0.96% Sitcom
    1239.7h 0.94% Börsenmagazin
    1185.5h 0.90% Wetterbericht
    1082.7h 0.82% Wirtschaftsmagazin
    1036.1h 0.79% Wissensmagazin
    1010.0h 0.77% Quiz
    993.7h  0.75% Musikmagazin
    952.0h  0.72% Dramaserie
    934.0h  0.71% Telenovela
    908.9h  0.69% Gesundheitsmagazin
    897.9h  0.68% Sportmagazin
