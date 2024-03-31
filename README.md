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

**102** channels, **785,301.6** hours playtime between **2023-01-17** and **2024-04-01**


### playtime per genre (top 30)

    51064.9h 6.50% Nachrichten
    37703.8h 4.80% Verkaufsshow
    31972.9h 4.07% Krimiserie
    27354.6h 3.48% Werbesendung
    24964.5h 3.18% Dokureihe
    23641.7h 3.01% Dokusoap
    22788.2h 2.90% Regionalmagazin
    20333.2h 2.59% Dokumentation
    20167.7h 2.57% *unknown*
    14440.5h 1.84% Zeichentrickserie
    14255.4h 1.82% Infomercial
    13945.1h 1.78% Animationsserie
    11895.5h 1.51% Comedyserie
    11103.5h 1.41% Morgenmagazin
    10797.8h 1.37% Magazin
    10618.3h 1.35% Religionsmagazin
    10473.2h 1.33% Talkshow
    7732.4h  0.98% E-Sport
    7372.4h  0.94% Programmende
    7304.6h  0.93% Sitcom
    6965.9h  0.89% Wetterbericht
    6951.6h  0.89% Börsenmagazin
    6704.3h  0.85% Quiz
    6699.9h  0.85% Komödie
    5842.6h  0.74% Wissensmagazin
    5693.5h  0.73% Politikmagazin
    5645.5h  0.72% Realityshow
    5637.5h  0.72% Wirtschaftsmagazin
    5598.6h  0.71% Telenovela
    5313.8h  0.68% Musikmagazin
