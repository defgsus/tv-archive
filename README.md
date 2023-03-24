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

**96** channels, **122,759.4** hours playtime between **2023-01-17** and **2023-03-25**


### playtime per genre (top 30)

    8663.8h 7.06% Nachrichten
    6174.6h 5.03% Verkaufsshow
    5134.4h 4.18% Krimiserie
    4133.6h 3.37% Werbesendung
    3862.5h 3.15% Dokusoap
    3774.5h 3.07% Dokureihe
    3650.1h 2.97% Regionalmagazin
    3005.3h 2.45% Dokumentation
    2838.3h 2.31% *unknown*
    2334.9h 1.90% Animationsserie
    2256.8h 1.84% Infomercial
    2233.7h 1.82% Zeichentrickserie
    2026.9h 1.65% Comedyserie
    1776.5h 1.45% Morgenmagazin
    1682.9h 1.37% Programmende
    1643.2h 1.34% Talkshow
    1589.0h 1.29% Religionsmagazin
    1273.2h 1.04% Magazin
    1262.3h 1.03% E-Sport
    1175.1h 0.96% Sitcom
    1162.2h 0.95% Börsenmagazin
    1097.6h 0.89% Wetterbericht
    1014.3h 0.83% Wirtschaftsmagazin
    965.9h  0.79% Wissensmagazin
    936.5h  0.76% Quiz
    917.4h  0.75% Musikmagazin
    897.7h  0.73% Dramaserie
    876.8h  0.71% Telenovela
    845.6h  0.69% Gesundheitsmagazin
    825.5h  0.67% Sportmagazin
