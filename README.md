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

**97** channels, **513,380.5** hours playtime between **2023-01-17** and **2023-10-29**


### playtime per genre (top 30)

    33842.1h 6.59% Nachrichten
    24485.8h 4.77% Verkaufsshow
    20655.5h 4.02% Krimiserie
    17363.9h 3.38% Werbesendung
    16882.8h 3.29% Dokureihe
    15633.1h 3.05% Dokusoap
    14804.1h 2.88% Regionalmagazin
    13022.4h 2.54% Dokumentation
    12329.2h 2.40% *unknown*
    9595.3h  1.87% Zeichentrickserie
    9346.3h  1.82% Infomercial
    9174.3h  1.79% Animationsserie
    8135.2h  1.58% Comedyserie
    7276.0h  1.42% Morgenmagazin
    6899.2h  1.34% Religionsmagazin
    6827.3h  1.33% Talkshow
    6459.1h  1.26% Magazin
    5262.9h  1.03% Programmende
    5039.1h  0.98% E-Sport
    4896.2h  0.95% Sitcom
    4761.5h  0.93% Wetterbericht
    4630.9h  0.90% Börsenmagazin
    4297.8h  0.84% Quiz
    4007.2h  0.78% Komödie
    3880.7h  0.76% Wissensmagazin
    3864.8h  0.75% Wirtschaftsmagazin
    3848.7h  0.75% Musikmagazin
    3684.5h  0.72% Telenovela
    3528.9h  0.69% Politikmagazin
    3403.9h  0.66% Realityshow
