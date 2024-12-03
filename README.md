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

**109** channels, **1,166,689.7** hours playtime between **2023-01-17** and **2024-12-04**


### playtime per genre (top 30)

    76206.4h 6.53% Nachrichten
    53157.8h 4.56% Verkaufsshow
    48695.9h 4.17% Krimiserie
    42999.0h 3.69% Werbesendung
    36365.3h 3.12% Dokureihe
    34658.0h 2.97% Dokusoap
    34136.2h 2.93% Regionalmagazin
    30710.4h 2.63% Dokumentation
    27469.6h 2.35% *unknown*
    21866.3h 1.87% Zeichentrickserie
    21569.0h 1.85% Infomercial
    20857.5h 1.79% Animationsserie
    16625.5h 1.43% Comedyserie
    16336.5h 1.40% Morgenmagazin
    15490.4h 1.33% Religionsmagazin
    15477.5h 1.33% Talkshow
    14488.9h 1.24% Magazin
    11524.4h 0.99% E-Sport
    11254.0h 0.96% Sitcom
    10543.8h 0.90% Wetterbericht
    10321.7h 0.88% Quiz
    10301.2h 0.88% Programmende
    10246.2h 0.88% Komödie
    8981.9h  0.77% Realityshow
    8882.5h  0.76% Politikmagazin
    8756.5h  0.75% Wissensmagazin
    8629.4h  0.74% Börsenmagazin
    7797.7h  0.67% Wirtschaftsmagazin
    7728.1h  0.66% Telenovela
    7720.2h  0.66% Dramaserie
