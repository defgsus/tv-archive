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

**109** channels, **997,859.6** hours playtime between **2023-01-17** and **2024-08-15**


### playtime per genre (top 30)

    64929.8h 6.51% Nachrichten
    46491.9h 4.66% Verkaufsshow
    40927.5h 4.10% Krimiserie
    35888.2h 3.60% Werbesendung
    31363.0h 3.14% Dokureihe
    30157.0h 3.02% Dokusoap
    29081.5h 2.91% Regionalmagazin
    26010.3h 2.61% Dokumentation
    24446.0h 2.45% *unknown*
    18492.5h 1.85% Zeichentrickserie
    18266.5h 1.83% Infomercial
    17859.1h 1.79% Animationsserie
    14697.0h 1.47% Comedyserie
    13998.7h 1.40% Morgenmagazin
    13565.6h 1.36% Religionsmagazin
    13496.0h 1.35% Magazin
    13087.2h 1.31% Talkshow
    9874.9h  0.99% E-Sport
    9493.2h  0.95% Sitcom
    9000.3h  0.90% Programmende
    8992.3h  0.90% Wetterbericht
    8730.4h  0.87% Komödie
    8590.9h  0.86% Quiz
    8101.5h  0.81% Börsenmagazin
    7475.8h  0.75% Politikmagazin
    7432.1h  0.74% Wissensmagazin
    7387.7h  0.74% Realityshow
    6836.4h  0.69% Wirtschaftsmagazin
    6567.7h  0.66% Telenovela
    6498.8h  0.65% Dramaserie
