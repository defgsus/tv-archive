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

**109** channels, **1,043,364.9** hours playtime between **2023-01-17** and **2024-09-13**


### playtime per genre (top 30)

    67910.1h 6.51% Nachrichten
    48458.5h 4.64% Verkaufsshow
    43024.7h 4.12% Krimiserie
    37798.7h 3.62% Werbesendung
    32764.3h 3.14% Dokureihe
    31432.3h 3.01% Dokusoap
    30490.9h 2.92% Regionalmagazin
    27296.3h 2.62% Dokumentation
    25135.2h 2.41% *unknown*
    19364.2h 1.86% Zeichentrickserie
    19133.2h 1.83% Infomercial
    18693.7h 1.79% Animationsserie
    15268.9h 1.46% Comedyserie
    14625.2h 1.40% Morgenmagazin
    14185.0h 1.36% Religionsmagazin
    13713.8h 1.31% Talkshow
    13640.0h 1.31% Magazin
    10314.9h 0.99% E-Sport
    9996.2h  0.96% Sitcom
    9441.6h  0.90% Wetterbericht
    9346.3h  0.90% Programmende
    9160.3h  0.88% Komödie
    9041.0h  0.87% Quiz
    8247.6h  0.79% Börsenmagazin
    7837.3h  0.75% Politikmagazin
    7818.4h  0.75% Wissensmagazin
    7794.4h  0.75% Realityshow
    7099.7h  0.68% Wirtschaftsmagazin
    6879.7h  0.66% Telenovela
    6802.6h  0.65% Dramaserie
