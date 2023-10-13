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

**97** channels, **486,065.9** hours playtime between **2023-01-17** and **2023-10-14**


### playtime per genre (top 30)

    32058.1h 6.60% Nachrichten
    23195.1h 4.77% Verkaufsshow
    19562.7h 4.02% Krimiserie
    16419.7h 3.38% Werbesendung
    16001.2h 3.29% Dokureihe
    14865.0h 3.06% Dokusoap
    14026.6h 2.89% Regionalmagazin
    12288.9h 2.53% Dokumentation
    11634.2h 2.39% *unknown*
    9112.1h  1.87% Zeichentrickserie
    8852.1h  1.82% Infomercial
    8657.2h  1.78% Animationsserie
    7777.3h  1.60% Comedyserie
    6890.2h  1.42% Morgenmagazin
    6519.6h  1.34% Religionsmagazin
    6459.8h  1.33% Talkshow
    6070.4h  1.25% Magazin
    5057.2h  1.04% Programmende
    4791.5h  0.99% E-Sport
    4627.4h  0.95% Sitcom
    4537.9h  0.93% Wetterbericht
    4386.2h  0.90% Börsenmagazin
    4092.5h  0.84% Quiz
    3763.6h  0.77% Komödie
    3697.7h  0.76% Musikmagazin
    3675.2h  0.76% Wirtschaftsmagazin
    3663.1h  0.75% Wissensmagazin
    3478.3h  0.72% Telenovela
    3304.4h  0.68% Politikmagazin
    3153.8h  0.65% Reportagereihe
