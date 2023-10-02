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

**97** channels, **466,346.0** hours playtime between **2023-01-17** and **2023-10-03**


### playtime per genre (top 30)

    30749.4h 6.59% Nachrichten
    22201.8h 4.76% Verkaufsshow
    18808.1h 4.03% Krimiserie
    15742.7h 3.38% Werbesendung
    15362.7h 3.29% Dokureihe
    14247.1h 3.06% Dokusoap
    13416.6h 2.88% Regionalmagazin
    11733.4h 2.52% Dokumentation
    11116.4h 2.38% *unknown*
    8762.1h  1.88% Zeichentrickserie
    8506.5h  1.82% Infomercial
    8279.6h  1.78% Animationsserie
    7500.4h  1.61% Comedyserie
    6593.1h  1.41% Morgenmagazin
    6259.0h  1.34% Religionsmagazin
    6182.0h  1.33% Talkshow
    5795.0h  1.24% Magazin
    4909.4h  1.05% Programmende
    4610.1h  0.99% E-Sport
    4410.8h  0.95% Sitcom
    4364.1h  0.94% Wetterbericht
    4213.7h  0.90% Börsenmagazin
    3908.4h  0.84% Quiz
    3614.0h  0.77% Komödie
    3587.0h  0.77% Musikmagazin
    3517.1h  0.75% Wirtschaftsmagazin
    3501.3h  0.75% Wissensmagazin
    3312.6h  0.71% Telenovela
    3122.4h  0.67% Politikmagazin
    3043.2h  0.65% Reportagereihe
