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

**97** channels, **606,322.5** hours playtime between **2023-01-17** and **2023-12-21**


### playtime per genre (top 30)

    39820.7h 6.57% Nachrichten
    29114.4h 4.80% Verkaufsshow
    24478.0h 4.04% Krimiserie
    20612.1h 3.40% Werbesendung
    19707.0h 3.25% Dokureihe
    18199.4h 3.00% Dokusoap
    17563.1h 2.90% Regionalmagazin
    15553.6h 2.57% Dokumentation
    14869.4h 2.45% *unknown*
    11199.9h 1.85% Zeichentrickserie
    11046.3h 1.82% Infomercial
    10731.2h 1.77% Animationsserie
    9284.8h  1.53% Comedyserie
    8656.6h  1.43% Morgenmagazin
    8219.9h  1.36% Religionsmagazin
    8116.8h  1.34% Talkshow
    7838.2h  1.29% Magazin
    5977.3h  0.99% Programmende
    5960.7h  0.98% E-Sport
    5888.6h  0.97% Sitcom
    5545.2h  0.91% Wetterbericht
    5478.9h  0.90% Börsenmagazin
    5023.9h  0.83% Quiz
    4750.6h  0.78% Komödie
    4621.4h  0.76% Wissensmagazin
    4521.9h  0.75% Wirtschaftsmagazin
    4409.3h  0.73% Telenovela
    4382.8h  0.72% Realityshow
    4377.7h  0.72% Musikmagazin
    4312.9h  0.71% Politikmagazin
