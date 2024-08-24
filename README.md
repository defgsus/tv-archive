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

**109** channels, **1,012,531.3** hours playtime between **2023-01-17** and **2024-08-25**


### playtime per genre (top 30)

    65859.5h 6.50% Nachrichten
    47144.7h 4.66% Verkaufsshow
    41620.2h 4.11% Krimiserie
    36495.4h 3.60% Werbesendung
    31832.6h 3.14% Dokureihe
    30609.4h 3.02% Dokusoap
    29513.7h 2.91% Regionalmagazin
    26431.7h 2.61% Dokumentation
    24697.1h 2.44% *unknown*
    18780.5h 1.85% Zeichentrickserie
    18545.8h 1.83% Infomercial
    18142.1h 1.79% Animationsserie
    14864.5h 1.47% Comedyserie
    14194.0h 1.40% Morgenmagazin
    13753.7h 1.36% Religionsmagazin
    13539.3h 1.34% Magazin
    13276.7h 1.31% Talkshow
    10004.7h 0.99% E-Sport
    9651.0h  0.95% Sitcom
    9143.1h  0.90% Wetterbericht
    9111.1h  0.90% Programmende
    8891.9h  0.88% Komödie
    8728.9h  0.86% Quiz
    8145.9h  0.80% Börsenmagazin
    7560.6h  0.75% Politikmagazin
    7535.7h  0.74% Wissensmagazin
    7496.9h  0.74% Realityshow
    6905.2h  0.68% Wirtschaftsmagazin
    6656.9h  0.66% Telenovela
    6603.1h  0.65% Dramaserie
