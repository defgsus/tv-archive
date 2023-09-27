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

**97** channels, **457,372.2** hours playtime between **2023-01-17** and **2023-09-28**


### playtime per genre (top 30)

    30194.8h 6.60% Nachrichten
    21744.2h 4.75% Verkaufsshow
    18475.3h 4.04% Krimiserie
    15438.3h 3.38% Werbesendung
    15074.8h 3.30% Dokureihe
    13945.2h 3.05% Dokusoap
    13188.2h 2.88% Regionalmagazin
    11493.3h 2.51% Dokumentation
    10887.0h 2.38% *unknown*
    8609.9h  1.88% Zeichentrickserie
    8340.8h  1.82% Infomercial
    8121.5h  1.78% Animationsserie
    7391.5h  1.62% Comedyserie
    6477.9h  1.42% Morgenmagazin
    6133.0h  1.34% Religionsmagazin
    6061.3h  1.33% Talkshow
    5703.2h  1.25% Magazin
    4839.9h  1.06% Programmende
    4508.3h  0.99% E-Sport
    4324.2h  0.95% Sitcom
    4294.4h  0.94% Wetterbericht
    4127.8h  0.90% Börsenmagazin
    3827.3h  0.84% Quiz
    3534.9h  0.77% Musikmagazin
    3516.9h  0.77% Komödie
    3460.3h  0.76% Wirtschaftsmagazin
    3433.9h  0.75% Wissensmagazin
    3251.2h  0.71% Telenovela
    3050.8h  0.67% Politikmagazin
    2996.2h  0.66% Reportagereihe
