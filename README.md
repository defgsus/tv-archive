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

**109** channels, **994,175.5** hours playtime between **2023-01-17** and **2024-08-13**


### playtime per genre (top 30)

    64654.1h 6.50% Nachrichten
    46334.4h 4.66% Verkaufsshow
    40744.4h 4.10% Krimiserie
    35738.7h 3.59% Werbesendung
    31255.9h 3.14% Dokureihe
    30045.6h 3.02% Dokusoap
    28938.4h 2.91% Regionalmagazin
    25903.0h 2.61% Dokumentation
    24391.7h 2.45% *unknown*
    18428.1h 1.85% Zeichentrickserie
    18198.2h 1.83% Infomercial
    17778.0h 1.79% Animationsserie
    14646.6h 1.47% Comedyserie
    13933.4h 1.40% Morgenmagazin
    13517.2h 1.36% Religionsmagazin
    13478.9h 1.36% Magazin
    13051.5h 1.31% Talkshow
    9838.6h  0.99% E-Sport
    9446.5h  0.95% Sitcom
    8972.8h  0.90% Programmende
    8951.6h  0.90% Wetterbericht
    8709.0h  0.88% Komödie
    8557.7h  0.86% Quiz
    8083.4h  0.81% Börsenmagazin
    7440.7h  0.75% Politikmagazin
    7398.1h  0.74% Wissensmagazin
    7355.2h  0.74% Realityshow
    6813.4h  0.69% Wirtschaftsmagazin
    6545.6h  0.66% Telenovela
    6462.4h  0.65% Dramaserie
