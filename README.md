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

**109** channels, **992,366.2** hours playtime between **2023-01-17** and **2024-08-12**


### playtime per genre (top 30)

    64515.3h 6.50% Nachrichten
    46253.8h 4.66% Verkaufsshow
    40656.1h 4.10% Krimiserie
    35664.8h 3.59% Werbesendung
    31212.1h 3.15% Dokureihe
    29997.6h 3.02% Dokusoap
    28864.3h 2.91% Regionalmagazin
    25846.7h 2.60% Dokumentation
    24372.5h 2.46% *unknown*
    18393.8h 1.85% Zeichentrickserie
    18166.5h 1.83% Infomercial
    17744.7h 1.79% Animationsserie
    14622.2h 1.47% Comedyserie
    13898.9h 1.40% Morgenmagazin
    13498.0h 1.36% Religionsmagazin
    13470.9h 1.36% Magazin
    13047.1h 1.31% Talkshow
    9818.6h  0.99% E-Sport
    9422.1h  0.95% Sitcom
    8959.9h  0.90% Programmende
    8931.6h  0.90% Wetterbericht
    8712.0h  0.88% Komödie
    8524.9h  0.86% Quiz
    8074.5h  0.81% Börsenmagazin
    7421.6h  0.75% Politikmagazin
    7391.8h  0.74% Wissensmagazin
    7340.7h  0.74% Realityshow
    6801.7h  0.69% Wirtschaftsmagazin
    6536.0h  0.66% Telenovela
    6445.9h  0.65% Dramaserie
