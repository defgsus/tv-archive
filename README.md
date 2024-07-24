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

**109** channels, **964,999.4** hours playtime between **2023-01-17** and **2024-07-25**


### playtime per genre (top 30)

    62863.7h 6.51% Nachrichten
    45050.9h 4.67% Verkaufsshow
    39565.0h 4.10% Krimiserie
    34509.3h 3.58% Werbesendung
    30346.2h 3.14% Dokureihe
    29224.7h 3.03% Dokusoap
    28094.6h 2.91% Regionalmagazin
    25102.1h 2.60% Dokumentation
    23996.0h 2.49% *unknown*
    17862.3h 1.85% Zeichentrickserie
    17640.5h 1.83% Infomercial
    17263.5h 1.79% Animationsserie
    14330.9h 1.49% Comedyserie
    13589.0h 1.41% Morgenmagazin
    13416.6h 1.39% Magazin
    13101.0h 1.36% Religionsmagazin
    12743.2h 1.32% Talkshow
    9562.1h  0.99% E-Sport
    9117.0h  0.94% Sitcom
    8745.4h  0.91% Programmende
    8663.6h  0.90% Wetterbericht
    8421.0h  0.87% Komödie
    8327.8h  0.86% Quiz
    7993.3h  0.83% Börsenmagazin
    7273.1h  0.75% Politikmagazin
    7172.2h  0.74% Wissensmagazin
    7165.0h  0.74% Realityshow
    6674.8h  0.69% Wirtschaftsmagazin
    6453.1h  0.67% Telenovela
    6292.9h  0.65% Dramaserie
