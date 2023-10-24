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

**97** channels, **505,741.8** hours playtime between **2023-01-17** and **2023-10-25**


### playtime per genre (top 30)

    33316.4h 6.59% Nachrichten
    24156.7h 4.78% Verkaufsshow
    20348.5h 4.02% Krimiserie
    17094.1h 3.38% Werbesendung
    16641.8h 3.29% Dokureihe
    15424.2h 3.05% Dokusoap
    14593.2h 2.89% Regionalmagazin
    12815.7h 2.53% Dokumentation
    12153.3h 2.40% *unknown*
    9456.3h  1.87% Zeichentrickserie
    9211.7h  1.82% Infomercial
    9032.2h  1.79% Animationsserie
    8027.8h  1.59% Comedyserie
    7160.8h  1.42% Morgenmagazin
    6801.4h  1.34% Religionsmagazin
    6732.9h  1.33% Talkshow
    6348.3h  1.26% Magazin
    5207.9h  1.03% Programmende
    4970.8h  0.98% E-Sport
    4822.6h  0.95% Sitcom
    4699.4h  0.93% Wetterbericht
    4570.4h  0.90% Börsenmagazin
    4244.6h  0.84% Quiz
    3929.3h  0.78% Komödie
    3821.9h  0.76% Wissensmagazin
    3809.8h  0.75% Wirtschaftsmagazin
    3809.1h  0.75% Musikmagazin
    3621.7h  0.72% Telenovela
    3479.5h  0.69% Politikmagazin
    3335.8h  0.66% Realityshow
