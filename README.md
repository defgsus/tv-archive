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

**109** channels, **974,037.2** hours playtime between **2023-01-17** and **2024-07-31**


### playtime per genre (top 30)

    63397.4h 6.51% Nachrichten
    45460.3h 4.67% Verkaufsshow
    39952.5h 4.10% Krimiserie
    34908.0h 3.58% Werbesendung
    30643.3h 3.15% Dokureihe
    29489.3h 3.03% Dokusoap
    28344.5h 2.91% Regionalmagazin
    25341.2h 2.60% Dokumentation
    24094.2h 2.47% *unknown*
    18036.0h 1.85% Zeichentrickserie
    17811.9h 1.83% Infomercial
    17432.0h 1.79% Animationsserie
    14432.1h 1.48% Comedyserie
    13691.5h 1.41% Morgenmagazin
    13437.9h 1.38% Magazin
    13236.2h 1.36% Religionsmagazin
    12841.9h 1.32% Talkshow
    9640.7h  0.99% E-Sport
    9214.9h  0.95% Sitcom
    8813.8h  0.90% Programmende
    8751.3h  0.90% Wetterbericht
    8525.8h  0.88% Komödie
    8395.9h  0.86% Quiz
    8019.9h  0.82% Börsenmagazin
    7325.2h  0.75% Politikmagazin
    7243.7h  0.74% Wissensmagazin
    7215.8h  0.74% Realityshow
    6716.6h  0.69% Wirtschaftsmagazin
    6478.2h  0.67% Telenovela
    6337.9h  0.65% Dramaserie
