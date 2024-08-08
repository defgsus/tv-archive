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

**109** channels, **988,723.6** hours playtime between **2023-01-17** and **2024-08-09**


### playtime per genre (top 30)

    64340.9h 6.51% Nachrichten
    46096.2h 4.66% Verkaufsshow
    40532.5h 4.10% Krimiserie
    35509.7h 3.59% Werbesendung
    31070.3h 3.14% Dokureihe
    29896.0h 3.02% Dokusoap
    28813.8h 2.91% Regionalmagazin
    25719.2h 2.60% Dokumentation
    24314.5h 2.46% *unknown*
    18326.5h 1.85% Zeichentrickserie
    18092.0h 1.83% Infomercial
    17681.5h 1.79% Animationsserie
    14598.7h 1.48% Comedyserie
    13890.7h 1.40% Morgenmagazin
    13463.8h 1.36% Magazin
    13434.3h 1.36% Religionsmagazin
    12989.1h 1.31% Talkshow
    9797.0h  0.99% E-Sport
    9383.0h  0.95% Sitcom
    8924.1h  0.90% Programmende
    8896.2h  0.90% Wetterbericht
    8657.0h  0.88% Komödie
    8507.4h  0.86% Quiz
    8074.3h  0.82% Börsenmagazin
    7424.7h  0.75% Politikmagazin
    7359.3h  0.74% Wissensmagazin
    7318.1h  0.74% Realityshow
    6797.8h  0.69% Wirtschaftsmagazin
    6531.6h  0.66% Telenovela
    6447.0h  0.65% Dramaserie
