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

**97** channels, **487,864.3** hours playtime between **2023-01-17** and **2023-10-15**


### playtime per genre (top 30)

    32135.2h 6.59% Nachrichten
    23282.4h 4.77% Verkaufsshow
    19640.8h 4.03% Krimiserie
    16488.0h 3.38% Werbesendung
    16055.4h 3.29% Dokureihe
    14907.3h 3.06% Dokusoap
    14054.4h 2.88% Regionalmagazin
    12333.0h 2.53% Dokumentation
    11683.3h 2.39% *unknown*
    9148.2h  1.88% Zeichentrickserie
    8886.6h  1.82% Infomercial
    8690.5h  1.78% Animationsserie
    7798.8h  1.60% Comedyserie
    6896.2h  1.41% Morgenmagazin
    6546.1h  1.34% Religionsmagazin
    6486.9h  1.33% Talkshow
    6090.4h  1.25% Magazin
    5069.8h  1.04% Programmende
    4802.5h  0.98% E-Sport
    4640.0h  0.95% Sitcom
    4549.1h  0.93% Wetterbericht
    4391.2h  0.90% Börsenmagazin
    4097.7h  0.84% Quiz
    3788.8h  0.78% Komödie
    3709.5h  0.76% Musikmagazin
    3679.6h  0.75% Wirtschaftsmagazin
    3673.2h  0.75% Wissensmagazin
    3481.7h  0.71% Telenovela
    3312.4h  0.68% Politikmagazin
    3168.9h  0.65% Reportagereihe
