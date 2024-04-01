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

**102** channels, **787,064.4** hours playtime between **2023-01-17** and **2024-04-02**


### playtime per genre (top 30)

    51169.8h 6.50% Nachrichten
    37768.6h 4.80% Verkaufsshow
    32017.7h 4.07% Krimiserie
    27414.2h 3.48% Werbesendung
    25047.5h 3.18% Dokureihe
    23698.6h 3.01% Dokusoap
    22821.8h 2.90% Regionalmagazin
    20412.7h 2.59% Dokumentation
    20214.0h 2.57% *unknown*
    14470.6h 1.84% Zeichentrickserie
    14275.6h 1.81% Infomercial
    13970.2h 1.77% Animationsserie
    11911.5h 1.51% Comedyserie
    11111.5h 1.41% Morgenmagazin
    10828.3h 1.38% Magazin
    10637.6h 1.35% Religionsmagazin
    10479.9h 1.33% Talkshow
    7753.4h  0.99% E-Sport
    7386.5h  0.94% Programmende
    7311.3h  0.93% Sitcom
    6981.6h  0.89% Wetterbericht
    6961.6h  0.88% Börsenmagazin
    6751.6h  0.86% Komödie
    6723.6h  0.85% Quiz
    5857.4h  0.74% Wissensmagazin
    5707.4h  0.73% Politikmagazin
    5666.8h  0.72% Realityshow
    5644.8h  0.72% Wirtschaftsmagazin
    5599.5h  0.71% Telenovela
    5317.9h  0.68% Musikmagazin
