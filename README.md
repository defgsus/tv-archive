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

**101** channels, **764,108.4** hours playtime between **2023-01-17** and **2024-03-19**


### playtime per genre (top 30)

    49726.7h 6.51% Nachrichten
    36698.2h 4.80% Verkaufsshow
    31135.9h 4.07% Krimiserie
    26520.7h 3.47% Werbesendung
    24332.9h 3.18% Dokureihe
    23098.0h 3.02% Dokusoap
    22192.2h 2.90% Regionalmagazin
    19737.0h 2.58% Dokumentation
    19611.7h 2.57% *unknown*
    14104.6h 1.85% Zeichentrickserie
    13900.5h 1.82% Infomercial
    13526.9h 1.77% Animationsserie
    11598.4h 1.52% Comedyserie
    10833.8h 1.42% Morgenmagazin
    10420.6h 1.36% Magazin
    10326.8h 1.35% Religionsmagazin
    10183.6h 1.33% Talkshow
    7523.4h  0.98% E-Sport
    7206.3h  0.94% Programmende
    7159.9h  0.94% Sitcom
    6787.1h  0.89% Wetterbericht
    6779.1h  0.89% Börsenmagazin
    6509.1h  0.85% Quiz
    6435.7h  0.84% Komödie
    5708.6h  0.75% Wissensmagazin
    5538.5h  0.72% Politikmagazin
    5528.6h  0.72% Realityshow
    5513.8h  0.72% Wirtschaftsmagazin
    5458.7h  0.71% Telenovela
    5197.5h  0.68% Musikmagazin
