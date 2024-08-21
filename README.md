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

**109** channels, **1,008,815.4** hours playtime between **2023-01-17** and **2024-08-22**


### playtime per genre (top 30)

    65634.8h 6.51% Nachrichten
    46972.6h 4.66% Verkaufsshow
    41449.7h 4.11% Krimiserie
    36329.9h 3.60% Werbesendung
    31708.5h 3.14% Dokureihe
    30502.1h 3.02% Dokusoap
    29421.7h 2.92% Regionalmagazin
    26315.9h 2.61% Dokumentation
    24614.5h 2.44% *unknown*
    18712.1h 1.85% Zeichentrickserie
    18470.3h 1.83% Infomercial
    18066.8h 1.79% Animationsserie
    14820.5h 1.47% Comedyserie
    14152.0h 1.40% Morgenmagazin
    13713.2h 1.36% Religionsmagazin
    13531.8h 1.34% Magazin
    13220.9h 1.31% Talkshow
    9978.5h  0.99% E-Sport
    9606.3h  0.95% Sitcom
    9104.8h  0.90% Wetterbericht
    9082.9h  0.90% Programmende
    8851.9h  0.88% Komödie
    8690.7h  0.86% Quiz
    8137.3h  0.81% Börsenmagazin
    7549.9h  0.75% Politikmagazin
    7515.8h  0.75% Wissensmagazin
    7471.6h  0.74% Realityshow
    6890.0h  0.68% Wirtschaftsmagazin
    6634.6h  0.66% Telenovela
    6577.1h  0.65% Dramaserie
