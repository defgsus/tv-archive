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

**97** channels, **394,928.2** hours playtime between **2023-01-17** and **2023-08-24**


### playtime per genre (top 30)

    26118.0h 6.61% Nachrichten
    18615.9h 4.71% Verkaufsshow
    16013.0h 4.05% Krimiserie
    13300.4h 3.37% Werbesendung
    13075.4h 3.31% Dokureihe
    11944.5h 3.02% Dokusoap
    11342.2h 2.87% Regionalmagazin
    9995.1h  2.53% Dokumentation
    9570.2h  2.42% *unknown*
    7457.3h  1.89% Zeichentrickserie
    7212.5h  1.83% Infomercial
    6980.7h  1.77% Animationsserie
    6450.1h  1.63% Comedyserie
    5569.4h  1.41% Morgenmagazin
    5261.5h  1.33% Religionsmagazin
    5189.9h  1.31% Talkshow
    4933.1h  1.25% Magazin
    4355.6h  1.10% Programmende
    3917.0h  0.99% E-Sport
    3732.5h  0.95% Wetterbericht
    3702.0h  0.94% Sitcom
    3567.3h  0.90% Börsenmagazin
    3205.2h  0.81% Quiz
    3116.5h  0.79% Musikmagazin
    3069.8h  0.78% Komödie
    3011.9h  0.76% Wirtschaftsmagazin
    2955.6h  0.75% Wissensmagazin
    2762.7h  0.70% Telenovela
    2604.5h  0.66% Reportagereihe
    2545.0h  0.64% Politikmagazin
