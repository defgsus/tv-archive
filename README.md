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

**97** channels, **475,315.0** hours playtime between **2023-01-17** and **2023-10-08**


### playtime per genre (top 30)

    31318.7h 6.59% Nachrichten
    22648.3h 4.76% Verkaufsshow
    19153.9h 4.03% Krimiserie
    16048.1h 3.38% Werbesendung
    15695.0h 3.30% Dokureihe
    14524.2h 3.06% Dokusoap
    13677.6h 2.88% Regionalmagazin
    11988.7h 2.52% Dokumentation
    11358.9h 2.39% *unknown*
    8925.0h  1.88% Zeichentrickserie
    8657.5h  1.82% Infomercial
    8451.5h  1.78% Animationsserie
    7627.8h  1.60% Comedyserie
    6710.4h  1.41% Morgenmagazin
    6371.4h  1.34% Religionsmagazin
    6301.9h  1.33% Talkshow
    5922.8h  1.25% Magazin
    4973.5h  1.05% Programmende
    4690.9h  0.99% E-Sport
    4506.9h  0.95% Sitcom
    4443.7h  0.93% Wetterbericht
    4283.9h  0.90% Börsenmagazin
    3978.6h  0.84% Quiz
    3702.3h  0.78% Komödie
    3636.6h  0.77% Musikmagazin
    3581.6h  0.75% Wirtschaftsmagazin
    3573.7h  0.75% Wissensmagazin
    3379.0h  0.71% Telenovela
    3200.0h  0.67% Politikmagazin
    3095.8h  0.65% Reportagereihe
