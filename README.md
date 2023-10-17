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

**97** channels, **493,236.5** hours playtime between **2023-01-17** and **2023-10-18**


### playtime per genre (top 30)

    32491.4h 6.59% Nachrichten
    23537.6h 4.77% Verkaufsshow
    19845.7h 4.02% Krimiserie
    16671.8h 3.38% Werbesendung
    16231.7h 3.29% Dokureihe
    15066.7h 3.05% Dokusoap
    14213.4h 2.88% Regionalmagazin
    12468.3h 2.53% Dokumentation
    11847.1h 2.40% *unknown*
    9238.4h  1.87% Zeichentrickserie
    8983.2h  1.82% Infomercial
    8792.9h  1.78% Animationsserie
    7867.6h  1.60% Comedyserie
    6972.5h  1.41% Morgenmagazin
    6636.8h  1.35% Religionsmagazin
    6561.4h  1.33% Talkshow
    6166.7h  1.25% Magazin
    5112.2h  1.04% Programmende
    4861.6h  0.99% E-Sport
    4693.3h  0.95% Sitcom
    4587.8h  0.93% Wetterbericht
    4449.5h  0.90% Börsenmagazin
    4144.3h  0.84% Quiz
    3832.0h  0.78% Komödie
    3740.0h  0.76% Musikmagazin
    3719.3h  0.75% Wirtschaftsmagazin
    3717.2h  0.75% Wissensmagazin
    3521.9h  0.71% Telenovela
    3366.1h  0.68% Politikmagazin
    3205.4h  0.65% Realityshow
