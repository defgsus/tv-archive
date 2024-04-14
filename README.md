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

**102** channels, **810,116.4** hours playtime between **2023-01-17** and **2024-04-15**


### playtime per genre (top 30)

    52679.6h 6.50% Nachrichten
    38874.6h 4.80% Verkaufsshow
    32943.7h 4.07% Krimiserie
    28291.8h 3.49% Werbesendung
    25709.9h 3.17% Dokureihe
    24399.0h 3.01% Dokusoap
    23512.6h 2.90% Regionalmagazin
    20983.9h 2.59% Dokumentation
    20822.2h 2.57% *unknown*
    14877.2h 1.84% Zeichentrickserie
    14701.4h 1.81% Infomercial
    14396.0h 1.78% Animationsserie
    12271.8h 1.51% Comedyserie
    11411.3h 1.41% Morgenmagazin
    11258.8h 1.39% Magazin
    10957.4h 1.35% Religionsmagazin
    10795.0h 1.33% Talkshow
    7981.3h  0.99% E-Sport
    7565.7h  0.93% Programmende
    7481.5h  0.92% Sitcom
    7187.2h  0.89% Wetterbericht
    7126.4h  0.88% Börsenmagazin
    6970.6h  0.86% Komödie
    6958.4h  0.86% Quiz
    6011.4h  0.74% Wissensmagazin
    5886.2h  0.73% Politikmagazin
    5826.5h  0.72% Realityshow
    5798.4h  0.72% Wirtschaftsmagazin
    5769.2h  0.71% Telenovela
    5435.2h  0.67% Musikmagazin
