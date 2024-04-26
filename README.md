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

**102** channels, **827,927.2** hours playtime between **2023-01-17** and **2024-04-27**


### playtime per genre (top 30)

    53987.3h 6.52% Nachrichten
    39694.4h 4.79% Verkaufsshow
    33734.3h 4.07% Krimiserie
    28934.6h 3.49% Werbesendung
    26163.6h 3.16% Dokureihe
    24971.5h 3.02% Dokusoap
    24106.3h 2.91% Regionalmagazin
    21396.0h 2.58% Dokumentation
    21166.7h 2.56% *unknown*
    15197.8h 1.84% Zeichentrickserie
    15039.3h 1.82% Infomercial
    14743.5h 1.78% Animationsserie
    12548.1h 1.52% Comedyserie
    11696.9h 1.41% Morgenmagazin
    11613.4h 1.40% Magazin
    11172.8h 1.35% Religionsmagazin
    11031.0h 1.33% Talkshow
    8196.1h  0.99% E-Sport
    7703.6h  0.93% Programmende
    7623.4h  0.92% Sitcom
    7348.8h  0.89% Wetterbericht
    7290.6h  0.88% Börsenmagazin
    7160.4h  0.86% Quiz
    7062.0h  0.85% Komödie
    6130.8h  0.74% Wissensmagazin
    6062.1h  0.73% Politikmagazin
    6002.4h  0.72% Realityshow
    5929.9h  0.72% Telenovela
    5929.0h  0.72% Wirtschaftsmagazin
    5521.1h  0.67% Musikmagazin
