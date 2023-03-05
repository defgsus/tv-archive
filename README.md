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

**96** channels, **88,434.7** hours playtime between **2023-01-17** and **2023-03-06**


### playtime per genre (top 30)

    6201.2h 7.01% Nachrichten
    4453.1h 5.04% Verkaufsshow
    3728.5h 4.22% Krimiserie
    3006.2h 3.40% Werbesendung
    2903.9h 3.28% Dokusoap
    2669.7h 3.02% Dokureihe
    2583.2h 2.92% Regionalmagazin
    2164.6h 2.45% Dokumentation
    2125.7h 2.40% *unknown*
    1682.1h 1.90% Animationsserie
    1618.1h 1.83% Infomercial
    1609.0h 1.82% Zeichentrickserie
    1418.9h 1.60% Comedyserie
    1245.2h 1.41% Morgenmagazin
    1214.0h 1.37% Programmende
    1166.4h 1.32% Religionsmagazin
    1155.4h 1.31% Talkshow
    935.0h  1.06% Magazin
    918.3h  1.04% E-Sport
    829.4h  0.94% Sitcom
    791.3h  0.89% Börsenmagazin
    774.8h  0.88% Wetterbericht
    715.4h  0.81% Wirtschaftsmagazin
    691.5h  0.78% Wissensmagazin
    649.2h  0.73% Musikmagazin
    647.0h  0.73% Quiz
    631.3h  0.71% Dramaserie
    624.0h  0.71% Gesundheitsmagazin
    593.2h  0.67% Telenovela
    573.6h  0.65% Sportmagazin
