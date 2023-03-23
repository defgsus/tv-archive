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

**96** channels, **120,976.4** hours playtime between **2023-01-17** and **2023-03-24**


### playtime per genre (top 30)

    8530.8h 7.05% Nachrichten
    6076.9h 5.02% Verkaufsshow
    5059.0h 4.18% Krimiserie
    4081.3h 3.37% Werbesendung
    3824.1h 3.16% Dokusoap
    3722.3h 3.08% Dokureihe
    3589.5h 2.97% Regionalmagazin
    2979.9h 2.46% Dokumentation
    2797.9h 2.31% *unknown*
    2302.9h 1.90% Animationsserie
    2224.1h 1.84% Infomercial
    2198.4h 1.82% Zeichentrickserie
    2000.0h 1.65% Comedyserie
    1741.8h 1.44% Morgenmagazin
    1668.9h 1.38% Programmende
    1616.0h 1.34% Talkshow
    1567.3h 1.30% Religionsmagazin
    1256.2h 1.04% Magazin
    1250.6h 1.03% E-Sport
    1159.0h 0.96% Sitcom
    1131.7h 0.94% Börsenmagazin
    1081.2h 0.89% Wetterbericht
    997.8h  0.82% Wirtschaftsmagazin
    952.5h  0.79% Wissensmagazin
    918.8h  0.76% Quiz
    906.4h  0.75% Musikmagazin
    877.1h  0.73% Dramaserie
    857.1h  0.71% Telenovela
    837.1h  0.69% Gesundheitsmagazin
    817.9h  0.68% Sportmagazin
