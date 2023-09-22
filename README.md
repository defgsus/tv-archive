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

**97** channels, **448,424.7** hours playtime between **2023-01-17** and **2023-09-23**


### playtime per genre (top 30)

    29633.5h 6.61% Nachrichten
    21342.1h 4.76% Verkaufsshow
    18146.4h 4.05% Krimiserie
    15124.1h 3.37% Werbesendung
    14772.6h 3.29% Dokureihe
    13657.5h 3.05% Dokusoap
    12938.6h 2.89% Regionalmagazin
    11261.4h 2.51% Dokumentation
    10664.0h 2.38% *unknown*
    8447.6h  1.88% Zeichentrickserie
    8179.9h  1.82% Infomercial
    7959.5h  1.77% Animationsserie
    7262.9h  1.62% Comedyserie
    6359.4h  1.42% Morgenmagazin
    5996.7h  1.34% Religionsmagazin
    5944.8h  1.33% Talkshow
    5591.2h  1.25% Magazin
    4770.7h  1.06% Programmende
    4425.1h  0.99% E-Sport
    4233.4h  0.94% Sitcom
    4218.2h  0.94% Wetterbericht
    4048.9h  0.90% Börsenmagazin
    3739.2h  0.83% Quiz
    3477.6h  0.78% Musikmagazin
    3460.4h  0.77% Komödie
    3402.1h  0.76% Wirtschaftsmagazin
    3360.2h  0.75% Wissensmagazin
    3190.4h  0.71% Telenovela
    2973.3h  0.66% Politikmagazin
    2944.3h  0.66% Reportagereihe
