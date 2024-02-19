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

**99** channels, **714,589.6** hours playtime between **2023-01-17** and **2024-02-20**


### playtime per genre (top 30)

    46522.6h 6.51% Nachrichten
    34303.2h 4.80% Verkaufsshow
    28942.1h 4.05% Krimiserie
    24613.2h 3.44% Werbesendung
    22944.3h 3.21% Dokureihe
    21557.6h 3.02% Dokusoap
    20678.3h 2.89% Regionalmagazin
    18445.8h 2.58% Dokumentation
    18120.4h 2.54% *unknown*
    13256.0h 1.86% Zeichentrickserie
    12989.7h 1.82% Infomercial
    12565.4h 1.76% Animationsserie
    10823.2h 1.51% Comedyserie
    10115.1h 1.42% Morgenmagazin
    9664.1h  1.35% Religionsmagazin
    9555.4h  1.34% Magazin
    9465.8h  1.32% Talkshow
    7047.9h  0.99% E-Sport
    6821.1h  0.95% Programmende
    6783.5h  0.95% Sitcom
    6365.2h  0.89% Börsenmagazin
    6356.7h  0.89% Wetterbericht
    6077.6h  0.85% Komödie
    5969.1h  0.84% Quiz
    5359.1h  0.75% Wissensmagazin
    5229.9h  0.73% Realityshow
    5185.3h  0.73% Wirtschaftsmagazin
    5120.1h  0.72% Politikmagazin
    5086.3h  0.71% Telenovela
    4944.5h  0.69% Musikmagazin
