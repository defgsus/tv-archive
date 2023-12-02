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

**97** channels, **574,047.6** hours playtime between **2023-01-17** and **2023-12-03**


### playtime per genre (top 30)

    37746.7h 6.58% Nachrichten
    27490.0h 4.79% Verkaufsshow
    23186.7h 4.04% Krimiserie
    19505.9h 3.40% Werbesendung
    18682.0h 3.25% Dokureihe
    17306.5h 3.01% Dokusoap
    16601.5h 2.89% Regionalmagazin
    14648.5h 2.55% Dokumentation
    14015.6h 2.44% *unknown*
    10624.0h 1.85% Zeichentrickserie
    10462.2h 1.82% Infomercial
    10210.3h 1.78% Animationsserie
    8908.5h  1.55% Comedyserie
    8176.2h  1.42% Morgenmagazin
    7753.6h  1.35% Religionsmagazin
    7676.3h  1.34% Talkshow
    7366.9h  1.28% Magazin
    5727.6h  1.00% Programmende
    5619.8h  0.98% E-Sport
    5532.1h  0.96% Sitcom
    5260.1h  0.92% Wetterbericht
    5199.4h  0.91% Börsenmagazin
    4777.7h  0.83% Quiz
    4443.7h  0.77% Komödie
    4367.4h  0.76% Wissensmagazin
    4298.2h  0.75% Wirtschaftsmagazin
    4196.1h  0.73% Musikmagazin
    4164.0h  0.73% Telenovela
    4064.1h  0.71% Realityshow
    4055.7h  0.71% Politikmagazin
