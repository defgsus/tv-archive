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

**102** channels, **833,036.9** hours playtime between **2023-01-17** and **2024-04-30**


### playtime per genre (top 30)

    54287.8h 6.52% Nachrichten
    39899.2h 4.79% Verkaufsshow
    33913.8h 4.07% Krimiserie
    29121.1h 3.50% Werbesendung
    26307.0h 3.16% Dokureihe
    25132.2h 3.02% Dokusoap
    24221.5h 2.91% Regionalmagazin
    21589.0h 2.59% Dokumentation
    21298.8h 2.56% *unknown*
    15301.5h 1.84% Zeichentrickserie
    15136.6h 1.82% Infomercial
    14834.3h 1.78% Animationsserie
    12602.2h 1.51% Comedyserie
    11740.0h 1.41% Morgenmagazin
    11704.8h 1.41% Magazin
    11252.4h 1.35% Religionsmagazin
    11088.2h 1.33% Talkshow
    8253.7h  0.99% E-Sport
    7745.5h  0.93% Programmende
    7661.0h  0.92% Sitcom
    7393.9h  0.89% Wetterbericht
    7317.8h  0.88% Börsenmagazin
    7204.7h  0.86% Quiz
    7104.9h  0.85% Komödie
    6164.6h  0.74% Wissensmagazin
    6101.6h  0.73% Politikmagazin
    6051.2h  0.73% Realityshow
    5952.1h  0.71% Wirtschaftsmagazin
    5946.5h  0.71% Telenovela
    5547.7h  0.67% Musikmagazin
