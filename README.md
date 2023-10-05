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

**97** channels, **471,728.0** hours playtime between **2023-01-17** and **2023-10-06**


### playtime per genre (top 30)

    31107.7h 6.59% Nachrichten
    22473.7h 4.76% Verkaufsshow
    19006.1h 4.03% Krimiserie
    15918.3h 3.37% Werbesendung
    15559.8h 3.30% Dokureihe
    14408.9h 3.05% Dokusoap
    13592.7h 2.88% Regionalmagazin
    11909.8h 2.52% Dokumentation
    11257.0h 2.39% *unknown*
    8856.4h  1.88% Zeichentrickserie
    8591.9h  1.82% Infomercial
    8383.8h  1.78% Animationsserie
    7578.1h  1.61% Comedyserie
    6670.1h  1.41% Morgenmagazin
    6326.6h  1.34% Religionsmagazin
    6247.1h  1.32% Talkshow
    5874.1h  1.25% Magazin
    4946.2h  1.05% Programmende
    4659.9h  0.99% E-Sport
    4475.2h  0.95% Sitcom
    4410.3h  0.93% Wetterbericht
    4250.2h  0.90% Börsenmagazin
    3954.4h  0.84% Quiz
    3657.7h  0.78% Komödie
    3616.6h  0.77% Musikmagazin
    3562.1h  0.76% Wirtschaftsmagazin
    3548.3h  0.75% Wissensmagazin
    3357.1h  0.71% Telenovela
    3187.1h  0.68% Politikmagazin
    3074.4h  0.65% Reportagereihe
