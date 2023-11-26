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

**97** channels, **565,040.8** hours playtime between **2023-01-17** and **2023-11-27**


### playtime per genre (top 30)

    37141.0h 6.57% Nachrichten
    27049.6h 4.79% Verkaufsshow
    22810.3h 4.04% Krimiserie
    19174.0h 3.39% Werbesendung
    18423.0h 3.26% Dokureihe
    17063.4h 3.02% Dokusoap
    16320.0h 2.89% Regionalmagazin
    14413.6h 2.55% Dokumentation
    13760.7h 2.44% *unknown*
    10462.6h 1.85% Zeichentrickserie
    10297.5h 1.82% Infomercial
    10058.5h 1.78% Animationsserie
    8799.4h  1.56% Comedyserie
    8028.4h  1.42% Morgenmagazin
    7639.5h  1.35% Religionsmagazin
    7561.7h  1.34% Talkshow
    7219.8h  1.28% Magazin
    5664.5h  1.00% Programmende
    5533.6h  0.98% E-Sport
    5425.2h  0.96% Sitcom
    5181.0h  0.92% Wetterbericht
    5124.9h  0.91% Börsenmagazin
    4698.7h  0.83% Quiz
    4388.1h  0.78% Komödie
    4294.4h  0.76% Wissensmagazin
    4234.4h  0.75% Wirtschaftsmagazin
    4146.8h  0.73% Musikmagazin
    4081.5h  0.72% Telenovela
    3966.2h  0.70% Politikmagazin
    3960.4h  0.70% Realityshow
