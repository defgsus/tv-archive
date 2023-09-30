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

**97** channels, **462,788.8** hours playtime between **2023-01-17** and **2023-10-01**


### playtime per genre (top 30)

    30537.4h 6.60% Nachrichten
    22024.1h 4.76% Verkaufsshow
    18688.3h 4.04% Krimiserie
    15619.6h 3.38% Werbesendung
    15242.3h 3.29% Dokureihe
    14119.3h 3.05% Dokusoap
    13331.5h 2.88% Regionalmagazin
    11629.6h 2.51% Dokumentation
    11022.7h 2.38% *unknown*
    8697.2h  1.88% Zeichentrickserie
    8444.4h  1.82% Infomercial
    8217.7h  1.78% Animationsserie
    7461.9h  1.61% Comedyserie
    6552.4h  1.42% Morgenmagazin
    6201.1h  1.34% Religionsmagazin
    6130.2h  1.32% Talkshow
    5759.6h  1.24% Magazin
    4881.3h  1.05% Programmende
    4572.7h  0.99% E-Sport
    4373.4h  0.95% Sitcom
    4337.8h  0.94% Wetterbericht
    4171.4h  0.90% Börsenmagazin
    3872.9h  0.84% Quiz
    3566.3h  0.77% Musikmagazin
    3564.1h  0.77% Komödie
    3493.6h  0.75% Wirtschaftsmagazin
    3474.0h  0.75% Wissensmagazin
    3294.0h  0.71% Telenovela
    3093.9h  0.67% Politikmagazin
    3026.4h  0.65% Reportagereihe
