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

**109** channels, **970,484.8** hours playtime between **2023-01-17** and **2024-07-29**


### playtime per genre (top 30)

    63154.0h 6.51% Nachrichten
    45308.2h 4.67% Verkaufsshow
    39784.2h 4.10% Krimiserie
    34757.0h 3.58% Werbesendung
    30537.0h 3.15% Dokureihe
    29385.0h 3.03% Dokusoap
    28213.8h 2.91% Regionalmagazin
    25232.1h 2.60% Dokumentation
    24073.6h 2.48% *unknown*
    17964.4h 1.85% Zeichentrickserie
    17748.5h 1.83% Infomercial
    17362.2h 1.79% Animationsserie
    14381.6h 1.48% Comedyserie
    13631.8h 1.40% Morgenmagazin
    13430.0h 1.38% Magazin
    13185.6h 1.36% Religionsmagazin
    12819.4h 1.32% Talkshow
    9613.4h  0.99% E-Sport
    9173.3h  0.95% Sitcom
    8786.9h  0.91% Programmende
    8715.0h  0.90% Wetterbericht
    8512.2h  0.88% Komödie
    8364.2h  0.86% Quiz
    8002.1h  0.82% Börsenmagazin
    7288.7h  0.75% Politikmagazin
    7219.9h  0.74% Wissensmagazin
    7191.8h  0.74% Realityshow
    6695.6h  0.69% Wirtschaftsmagazin
    6465.1h  0.67% Telenovela
    6322.4h  0.65% Dramaserie
