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

**97** channels, **491,441.5** hours playtime between **2023-01-17** and **2023-10-17**


### playtime per genre (top 30)

    32364.5h 6.59% Nachrichten
    23445.2h 4.77% Verkaufsshow
    19760.2h 4.02% Krimiserie
    16614.7h 3.38% Werbesendung
    16169.1h 3.29% Dokureihe
    15021.0h 3.06% Dokusoap
    14149.0h 2.88% Regionalmagazin
    12427.0h 2.53% Dokumentation
    11804.2h 2.40% *unknown*
    9208.7h  1.87% Zeichentrickserie
    8949.4h  1.82% Infomercial
    8755.4h  1.78% Animationsserie
    7839.8h  1.60% Comedyserie
    6937.3h  1.41% Morgenmagazin
    6605.9h  1.34% Religionsmagazin
    6539.8h  1.33% Talkshow
    6146.8h  1.25% Magazin
    5097.4h  1.04% Programmende
    4841.3h  0.99% E-Sport
    4675.8h  0.95% Sitcom
    4571.6h  0.93% Wetterbericht
    4420.3h  0.90% Börsenmagazin
    4129.8h  0.84% Quiz
    3819.7h  0.78% Komödie
    3729.8h  0.76% Musikmagazin
    3705.3h  0.75% Wirtschaftsmagazin
    3702.7h  0.75% Wissensmagazin
    3500.8h  0.71% Telenovela
    3343.3h  0.68% Politikmagazin
    3192.2h  0.65% Reportagereihe
