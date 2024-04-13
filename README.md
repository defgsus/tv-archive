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

**102** channels, **808,355.0** hours playtime between **2023-01-17** and **2024-04-14**


### playtime per genre (top 30)

    52597.3h 6.51% Nachrichten
    38814.2h 4.80% Verkaufsshow
    32891.4h 4.07% Krimiserie
    28212.5h 3.49% Werbesendung
    25625.4h 3.17% Dokureihe
    24359.9h 3.01% Dokusoap
    23479.5h 2.90% Regionalmagazin
    20934.3h 2.59% Dokumentation
    20767.4h 2.57% *unknown*
    14842.7h 1.84% Zeichentrickserie
    14669.5h 1.81% Infomercial
    14364.9h 1.78% Animationsserie
    12256.8h 1.52% Comedyserie
    11404.1h 1.41% Morgenmagazin
    11218.6h 1.39% Magazin
    10918.4h 1.35% Religionsmagazin
    10759.9h 1.33% Talkshow
    7956.4h  0.98% E-Sport
    7551.4h  0.93% Programmende
    7470.3h  0.92% Sitcom
    7175.4h  0.89% Wetterbericht
    7118.4h  0.88% Börsenmagazin
    6952.3h  0.86% Quiz
    6933.3h  0.86% Komödie
    5993.6h  0.74% Wissensmagazin
    5880.4h  0.73% Politikmagazin
    5815.4h  0.72% Realityshow
    5790.5h  0.72% Wirtschaftsmagazin
    5768.8h  0.71% Telenovela
    5423.7h  0.67% Musikmagazin
