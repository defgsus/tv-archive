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

**97** channels, **574,025.4** hours playtime between **2023-01-17** and **2023-12-02**


### playtime per genre (top 30)

    37789.6h 6.58% Nachrichten
    27506.3h 4.79% Verkaufsshow
    23206.3h 4.04% Krimiserie
    19497.7h 3.40% Werbesendung
    18679.4h 3.25% Dokureihe
    17331.0h 3.02% Dokusoap
    16641.3h 2.90% Regionalmagazin
    14637.0h 2.55% Dokumentation
    13994.2h 2.44% *unknown*
    10610.0h 1.85% Zeichentrickserie
    10457.7h 1.82% Infomercial
    10207.8h 1.78% Animationsserie
    8924.2h  1.55% Comedyserie
    8201.1h  1.43% Morgenmagazin
    7744.0h  1.35% Religionsmagazin
    7686.9h  1.34% Talkshow
    7357.9h  1.28% Magazin
    5734.0h  1.00% Programmende
    5623.4h  0.98% E-Sport
    5531.8h  0.96% Sitcom
    5260.6h  0.92% Wetterbericht
    5220.1h  0.91% Börsenmagazin
    4786.4h  0.83% Quiz
    4423.5h  0.77% Komödie
    4373.3h  0.76% Wissensmagazin
    4311.6h  0.75% Wirtschaftsmagazin
    4189.1h  0.73% Musikmagazin
    4179.3h  0.73% Telenovela
    4079.3h  0.71% Realityshow
    4073.3h  0.71% Politikmagazin
