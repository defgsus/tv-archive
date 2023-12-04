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

**97** channels, **577,606.6** hours playtime between **2023-01-17** and **2023-12-05**


### playtime per genre (top 30)

    37961.7h 6.57% Nachrichten
    27664.1h 4.79% Verkaufsshow
    23296.9h 4.03% Krimiserie
    19630.9h 3.40% Werbesendung
    18812.0h 3.26% Dokureihe
    17419.5h 3.02% Dokusoap
    16686.9h 2.89% Regionalmagazin
    14752.8h 2.55% Dokumentation
    14115.6h 2.44% *unknown*
    10681.9h 1.85% Zeichentrickserie
    10524.9h 1.82% Infomercial
    10270.2h 1.78% Animationsserie
    8943.8h  1.55% Comedyserie
    8217.7h  1.42% Morgenmagazin
    7813.4h  1.35% Religionsmagazin
    7729.9h  1.34% Talkshow
    7415.0h  1.28% Magazin
    5756.4h  1.00% Programmende
    5657.5h  0.98% E-Sport
    5563.4h  0.96% Sitcom
    5291.1h  0.92% Wetterbericht
    5229.7h  0.91% Börsenmagazin
    4801.6h  0.83% Quiz
    4471.4h  0.77% Komödie
    4395.6h  0.76% Wissensmagazin
    4320.8h  0.75% Wirtschaftsmagazin
    4215.1h  0.73% Musikmagazin
    4182.7h  0.72% Telenovela
    4094.0h  0.71% Realityshow
    4080.5h  0.71% Politikmagazin
