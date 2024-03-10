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

**101** channels, **750,103.7** hours playtime between **2023-01-17** and **2024-03-11**


### playtime per genre (top 30)

    48780.9h 6.50% Nachrichten
    36026.8h 4.80% Verkaufsshow
    30522.1h 4.07% Krimiserie
    25992.3h 3.47% Werbesendung
    23977.5h 3.20% Dokureihe
    22668.5h 3.02% Dokusoap
    21751.3h 2.90% Regionalmagazin
    19335.9h 2.58% Dokumentation
    19255.6h 2.57% *unknown*
    13871.5h 1.85% Zeichentrickserie
    13641.9h 1.82% Infomercial
    13232.4h 1.76% Animationsserie
    11376.1h 1.52% Comedyserie
    10625.4h 1.42% Morgenmagazin
    10158.6h 1.35% Magazin
    10143.7h 1.35% Religionsmagazin
    9993.4h  1.33% Talkshow
    7406.5h  0.99% E-Sport
    7096.4h  0.95% Programmende
    7050.5h  0.94% Sitcom
    6669.6h  0.89% Börsenmagazin
    6661.1h  0.89% Wetterbericht
    6358.3h  0.85% Komödie
    6342.6h  0.85% Quiz
    5608.6h  0.75% Wissensmagazin
    5441.7h  0.73% Realityshow
    5420.9h  0.72% Wirtschaftsmagazin
    5398.4h  0.72% Politikmagazin
    5345.3h  0.71% Telenovela
    5130.8h  0.68% Musikmagazin
