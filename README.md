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

**99** channels, **655,963.7** hours playtime between **2023-01-17** and **2024-01-18**


### playtime per genre (top 30)

    42802.9h 6.53% Nachrichten
    31332.8h 4.78% Verkaufsshow
    26336.9h 4.01% Krimiserie
    22370.9h 3.41% Werbesendung
    21309.8h 3.25% Dokureihe
    19606.5h 2.99% Dokusoap
    18891.8h 2.88% Regionalmagazin
    17007.2h 2.59% Dokumentation
    16357.3h 2.49% *unknown*
    12122.8h 1.85% Zeichentrickserie
    11907.9h 1.82% Infomercial
    11530.7h 1.76% Animationsserie
    9935.9h  1.51% Comedyserie
    9281.7h  1.41% Morgenmagazin
    8869.0h  1.35% Religionsmagazin
    8692.9h  1.33% Magazin
    8670.3h  1.32% Talkshow
    6450.2h  0.98% E-Sport
    6357.0h  0.97% Programmende
    6331.9h  0.97% Sitcom
    5928.3h  0.90% Wetterbericht
    5832.7h  0.89% Börsenmagazin
    5562.8h  0.85% Komödie
    5419.8h  0.83% Quiz
    4936.9h  0.75% Wissensmagazin
    4803.1h  0.73% Wirtschaftsmagazin
    4764.6h  0.73% Realityshow
    4675.3h  0.71% Telenovela
    4652.3h  0.71% Musikmagazin
    4629.1h  0.71% Politikmagazin
