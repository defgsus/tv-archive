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

**102** channels, **839,870.4** hours playtime between **2023-01-17** and **2024-05-06**


### playtime per genre (top 30)

    54744.3h 6.52% Nachrichten
    40160.8h 4.78% Verkaufsshow
    34161.6h 4.07% Krimiserie
    29370.7h 3.50% Werbesendung
    26545.2h 3.16% Dokureihe
    25372.8h 3.02% Dokusoap
    24402.9h 2.91% Regionalmagazin
    21776.0h 2.59% Dokumentation
    21437.4h 2.55% *unknown*
    15439.7h 1.84% Zeichentrickserie
    15264.5h 1.82% Infomercial
    14953.6h 1.78% Animationsserie
    12688.7h 1.51% Comedyserie
    11839.6h 1.41% Magazin
    11816.4h 1.41% Morgenmagazin
    11354.0h 1.35% Religionsmagazin
    11189.6h 1.33% Talkshow
    8329.4h  0.99% E-Sport
    7800.8h  0.93% Programmende
    7717.9h  0.92% Sitcom
    7455.8h  0.89% Wetterbericht
    7401.4h  0.88% Börsenmagazin
    7244.0h  0.86% Quiz
    7207.4h  0.86% Komödie
    6210.1h  0.74% Wissensmagazin
    6148.8h  0.73% Politikmagazin
    6135.3h  0.73% Realityshow
    5999.2h  0.71% Wirtschaftsmagazin
    5983.8h  0.71% Telenovela
    5588.3h  0.67% Musikmagazin
