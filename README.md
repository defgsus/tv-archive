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

**109** channels, **1,097,941.8** hours playtime between **2023-01-17** and **2024-10-20**


### playtime per genre (top 30)

    71473.2h 6.51% Nachrichten
    50641.2h 4.61% Verkaufsshow
    45554.2h 4.15% Krimiserie
    40147.2h 3.66% Werbesendung
    34367.0h 3.13% Dokureihe
    32873.7h 2.99% Dokusoap
    32085.8h 2.92% Regionalmagazin
    28760.1h 2.62% Dokumentation
    26129.9h 2.38% *unknown*
    20468.9h 1.86% Zeichentrickserie
    20197.2h 1.84% Infomercial
    19653.4h 1.79% Animationsserie
    15899.8h 1.45% Comedyserie
    15357.6h 1.40% Morgenmagazin
    14819.9h 1.35% Religionsmagazin
    14505.9h 1.32% Talkshow
    13994.7h 1.27% Magazin
    10862.0h 0.99% E-Sport
    10571.3h 0.96% Sitcom
    9945.0h  0.91% Wetterbericht
    9761.6h  0.89% Programmende
    9626.6h  0.88% Komödie
    9623.9h  0.88% Quiz
    8410.8h  0.77% Börsenmagazin
    8337.8h  0.76% Realityshow
    8285.5h  0.75% Politikmagazin
    8246.1h  0.75% Wissensmagazin
    7395.2h  0.67% Wirtschaftsmagazin
    7237.4h  0.66% Telenovela
    7180.3h  0.65% Dramaserie
