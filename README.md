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

**96** channels, **142,813.3** hours playtime between **2023-01-17** and **2023-04-06**


### playtime per genre (top 30)

    9949.9h 6.97% Nachrichten
    7105.2h 4.98% Verkaufsshow
    5955.7h 4.17% Krimiserie
    4808.1h 3.37% Werbesendung
    4518.8h 3.16% Dokureihe
    4375.1h 3.06% Dokusoap
    4209.6h 2.95% Regionalmagazin
    3546.9h 2.48% Dokumentation
    3303.8h 2.31% *unknown*
    2691.9h 1.88% Animationsserie
    2634.6h 1.84% Infomercial
    2617.0h 1.83% Zeichentrickserie
    2364.9h 1.66% Comedyserie
    2041.1h 1.43% Morgenmagazin
    1975.7h 1.38% Programmende
    1889.5h 1.32% Talkshow
    1862.2h 1.30% Religionsmagazin
    1523.1h 1.07% Magazin
    1471.7h 1.03% E-Sport
    1372.1h 0.96% Sitcom
    1347.0h 0.94% Börsenmagazin
    1280.4h 0.90% Wetterbericht
    1169.0h 0.82% Wirtschaftsmagazin
    1124.2h 0.79% Wissensmagazin
    1091.4h 0.76% Quiz
    1078.9h 0.76% Musikmagazin
    1011.9h 0.71% Telenovela
    1007.5h 0.71% Dramaserie
    989.6h  0.69% Gesundheitsmagazin
    984.9h  0.69% Sportmagazin
