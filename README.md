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

**97** channels, **611,715.1** hours playtime between **2023-01-17** and **2023-12-24**


### playtime per genre (top 30)

    40151.8h 6.56% Nachrichten
    29355.6h 4.80% Verkaufsshow
    24684.4h 4.04% Krimiserie
    20807.1h 3.40% Werbesendung
    19880.4h 3.25% Dokureihe
    18332.7h 3.00% Dokusoap
    17713.4h 2.90% Regionalmagazin
    15706.2h 2.57% Dokumentation
    15022.8h 2.46% *unknown*
    11299.4h 1.85% Zeichentrickserie
    11143.1h 1.82% Infomercial
    10810.2h 1.77% Animationsserie
    9360.1h  1.53% Comedyserie
    8732.0h  1.43% Morgenmagazin
    8290.0h  1.36% Religionsmagazin
    8166.2h  1.33% Talkshow
    7933.2h  1.30% Magazin
    6018.2h  0.98% Programmende
    6016.9h  0.98% E-Sport
    5934.0h  0.97% Sitcom
    5593.4h  0.91% Wetterbericht
    5506.8h  0.90% Börsenmagazin
    5058.6h  0.83% Quiz
    4863.1h  0.79% Komödie
    4655.0h  0.76% Wissensmagazin
    4554.8h  0.74% Wirtschaftsmagazin
    4449.2h  0.73% Telenovela
    4432.7h  0.72% Realityshow
    4405.0h  0.72% Musikmagazin
    4336.6h  0.71% Politikmagazin
