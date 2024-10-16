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

**109** channels, **1,094,357.4** hours playtime between **2023-01-17** and **2024-10-17**


### playtime per genre (top 30)

    71257.7h 6.51% Nachrichten
    50490.4h 4.61% Verkaufsshow
    45384.7h 4.15% Krimiserie
    39991.8h 3.65% Werbesendung
    34254.7h 3.13% Dokureihe
    32774.1h 2.99% Dokusoap
    32001.3h 2.92% Regionalmagazin
    28661.8h 2.62% Dokumentation
    26067.9h 2.38% *unknown*
    20396.5h 1.86% Zeichentrickserie
    20123.8h 1.84% Infomercial
    19579.5h 1.79% Animationsserie
    15862.4h 1.45% Comedyserie
    15319.4h 1.40% Morgenmagazin
    14789.3h 1.35% Religionsmagazin
    14453.1h 1.32% Talkshow
    13969.2h 1.28% Magazin
    10822.5h 0.99% E-Sport
    10532.9h 0.96% Sitcom
    9911.5h  0.91% Wetterbericht
    9733.6h  0.89% Programmende
    9603.8h  0.88% Komödie
    9593.9h  0.88% Quiz
    8402.8h  0.77% Börsenmagazin
    8314.9h  0.76% Realityshow
    8257.8h  0.75% Politikmagazin
    8230.2h  0.75% Wissensmagazin
    7377.2h  0.67% Wirtschaftsmagazin
    7216.8h  0.66% Telenovela
    7158.0h  0.65% Dramaserie
