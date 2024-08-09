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

**109** channels, **988,739.0** hours playtime between **2023-01-17** and **2024-08-10**


### playtime per genre (top 30)

    64338.0h 6.51% Nachrichten
    46095.6h 4.66% Verkaufsshow
    40530.2h 4.10% Krimiserie
    35512.9h 3.59% Werbesendung
    31058.9h 3.14% Dokureihe
    29912.5h 3.03% Dokusoap
    28805.7h 2.91% Regionalmagazin
    25725.9h 2.60% Dokumentation
    24306.7h 2.46% *unknown*
    18328.2h 1.85% Zeichentrickserie
    18093.2h 1.83% Infomercial
    17677.2h 1.79% Animationsserie
    14605.1h 1.48% Comedyserie
    13890.9h 1.40% Morgenmagazin
    13458.9h 1.36% Magazin
    13435.0h 1.36% Religionsmagazin
    12995.7h 1.31% Talkshow
    9812.5h  0.99% E-Sport
    9382.0h  0.95% Sitcom
    8924.2h  0.90% Programmende
    8896.1h  0.90% Wetterbericht
    8656.3h  0.88% Komödie
    8510.9h  0.86% Quiz
    8074.5h  0.82% Börsenmagazin
    7416.6h  0.75% Politikmagazin
    7351.2h  0.74% Wissensmagazin
    7316.8h  0.74% Realityshow
    6794.9h  0.69% Wirtschaftsmagazin
    6535.1h  0.66% Telenovela
    6447.0h  0.65% Dramaserie
