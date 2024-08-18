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

**109** channels, **1,003,376.6** hours playtime between **2023-01-17** and **2024-08-19**


### playtime per genre (top 30)

    65234.1h 6.50% Nachrichten
    46747.7h 4.66% Verkaufsshow
    41170.4h 4.10% Krimiserie
    36105.2h 3.60% Werbesendung
    31567.2h 3.15% Dokureihe
    30323.7h 3.02% Dokusoap
    29214.9h 2.91% Regionalmagazin
    26174.6h 2.61% Dokumentation
    24543.0h 2.45% *unknown*
    18598.6h 1.85% Zeichentrickserie
    18375.1h 1.83% Infomercial
    17964.9h 1.79% Animationsserie
    14749.2h 1.47% Comedyserie
    14048.2h 1.40% Morgenmagazin
    13648.1h 1.36% Religionsmagazin
    13518.0h 1.35% Magazin
    13171.7h 1.31% Talkshow
    9927.9h  0.99% E-Sport
    9540.5h  0.95% Sitcom
    9044.5h  0.90% Wetterbericht
    9042.5h  0.90% Programmende
    8806.8h  0.88% Komödie
    8630.1h  0.86% Quiz
    8110.9h  0.81% Börsenmagazin
    7493.5h  0.75% Politikmagazin
    7478.1h  0.75% Wissensmagazin
    7424.6h  0.74% Realityshow
    6851.3h  0.68% Wirtschaftsmagazin
    6582.2h  0.66% Telenovela
    6526.2h  0.65% Dramaserie
