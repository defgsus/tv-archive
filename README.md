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

**97** channels, **469,929.6** hours playtime between **2023-01-17** and **2023-10-05**


### playtime per genre (top 30)

    30976.8h 6.59% Nachrichten
    22380.6h 4.76% Verkaufsshow
    18928.8h 4.03% Krimiserie
    15862.6h 3.38% Werbesendung
    15512.4h 3.30% Dokureihe
    14347.8h 3.05% Dokusoap
    13525.8h 2.88% Regionalmagazin
    11859.4h 2.52% Dokumentation
    11206.6h 2.38% *unknown*
    8824.9h  1.88% Zeichentrickserie
    8559.5h  1.82% Infomercial
    8351.3h  1.78% Animationsserie
    7558.4h  1.61% Comedyserie
    6635.4h  1.41% Morgenmagazin
    6303.9h  1.34% Religionsmagazin
    6231.0h  1.33% Talkshow
    5841.2h  1.24% Magazin
    4931.8h  1.05% Programmende
    4640.2h  0.99% E-Sport
    4451.2h  0.95% Sitcom
    4394.5h  0.94% Wetterbericht
    4237.9h  0.90% Börsenmagazin
    3937.5h  0.84% Quiz
    3651.9h  0.78% Komödie
    3606.6h  0.77% Musikmagazin
    3545.3h  0.75% Wirtschaftsmagazin
    3533.6h  0.75% Wissensmagazin
    3337.9h  0.71% Telenovela
    3168.4h  0.67% Politikmagazin
    3065.9h  0.65% Reportagereihe
