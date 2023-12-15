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

**97** channels, **597,330.7** hours playtime between **2023-01-17** and **2023-12-16**


### playtime per genre (top 30)

    39266.5h 6.57% Nachrichten
    28676.8h 4.80% Verkaufsshow
    24167.4h 4.05% Krimiserie
    20300.1h 3.40% Werbesendung
    19417.5h 3.25% Dokureihe
    17958.1h 3.01% Dokusoap
    17307.8h 2.90% Regionalmagazin
    15286.0h 2.56% Dokumentation
    14624.4h 2.45% *unknown*
    11026.1h 1.85% Zeichentrickserie
    10886.4h 1.82% Infomercial
    10591.5h 1.77% Animationsserie
    9181.3h  1.54% Comedyserie
    8540.4h  1.43% Morgenmagazin
    8085.3h  1.35% Religionsmagazin
    8005.5h  1.34% Talkshow
    7709.8h  1.29% Magazin
    5908.4h  0.99% Programmende
    5869.2h  0.98% E-Sport
    5790.1h  0.97% Sitcom
    5467.0h  0.92% Wetterbericht
    5409.4h  0.91% Börsenmagazin
    4963.6h  0.83% Quiz
    4632.8h  0.78% Komödie
    4557.9h  0.76% Wissensmagazin
    4468.1h  0.75% Wirtschaftsmagazin
    4350.6h  0.73% Telenovela
    4326.4h  0.72% Musikmagazin
    4316.1h  0.72% Realityshow
    4253.1h  0.71% Politikmagazin
