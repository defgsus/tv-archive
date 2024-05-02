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

**102** channels, **838,135.7** hours playtime between **2023-01-17** and **2024-05-03**


### playtime per genre (top 30)

    54679.2h 6.52% Nachrichten
    40095.2h 4.78% Verkaufsshow
    34123.8h 4.07% Krimiserie
    29303.2h 3.50% Werbesendung
    26483.3h 3.16% Dokureihe
    25297.7h 3.02% Dokusoap
    24373.6h 2.91% Regionalmagazin
    21741.2h 2.59% Dokumentation
    21380.3h 2.55% *unknown*
    15409.5h 1.84% Zeichentrickserie
    15226.9h 1.82% Infomercial
    14923.7h 1.78% Animationsserie
    12677.0h 1.51% Comedyserie
    11811.5h 1.41% Magazin
    11809.4h 1.41% Morgenmagazin
    11313.1h 1.35% Religionsmagazin
    11156.4h 1.33% Talkshow
    8303.7h  0.99% E-Sport
    7787.1h  0.93% Programmende
    7709.9h  0.92% Sitcom
    7443.8h  0.89% Wetterbericht
    7366.9h  0.88% Börsenmagazin
    7242.1h  0.86% Quiz
    7155.4h  0.85% Komödie
    6196.9h  0.74% Wissensmagazin
    6148.6h  0.73% Politikmagazin
    6131.9h  0.73% Realityshow
    5992.3h  0.71% Wirtschaftsmagazin
    5982.2h  0.71% Telenovela
    5576.5h  0.67% Musikmagazin
