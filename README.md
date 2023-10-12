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

**97** channels, **484,275.5** hours playtime between **2023-01-17** and **2023-10-13**


### playtime per genre (top 30)

    31931.8h 6.59% Nachrichten
    23098.6h 4.77% Verkaufsshow
    19490.3h 4.02% Krimiserie
    16361.8h 3.38% Werbesendung
    15941.5h 3.29% Dokureihe
    14816.2h 3.06% Dokusoap
    13964.8h 2.88% Regionalmagazin
    12242.2h 2.53% Dokumentation
    11585.7h 2.39% *unknown*
    9083.5h  1.88% Zeichentrickserie
    8820.6h  1.82% Infomercial
    8622.0h  1.78% Animationsserie
    7749.1h  1.60% Comedyserie
    6855.9h  1.42% Morgenmagazin
    6501.8h  1.34% Religionsmagazin
    6430.4h  1.33% Talkshow
    6026.6h  1.24% Magazin
    5042.8h  1.04% Programmende
    4776.7h  0.99% E-Sport
    4610.5h  0.95% Sitcom
    4523.0h  0.93% Wetterbericht
    4374.6h  0.90% Börsenmagazin
    4071.0h  0.84% Quiz
    3747.5h  0.77% Komödie
    3690.5h  0.76% Musikmagazin
    3657.0h  0.76% Wirtschaftsmagazin
    3650.8h  0.75% Wissensmagazin
    3458.6h  0.71% Telenovela
    3296.5h  0.68% Politikmagazin
    3147.5h  0.65% Reportagereihe
