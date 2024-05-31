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

**108** channels, **879,916.3** hours playtime between **2023-01-17** and **2024-06-01**


### playtime per genre (top 30)

    57517.2h 6.54% Nachrichten
    41744.8h 4.74% Verkaufsshow
    35824.6h 4.07% Krimiserie
    30890.2h 3.51% Werbesendung
    27703.0h 3.15% Dokureihe
    26610.6h 3.02% Dokusoap
    25588.2h 2.91% Regionalmagazin
    22834.9h 2.60% Dokumentation
    22270.4h 2.53% *unknown*
    16172.0h 1.84% Zeichentrickserie
    16003.5h 1.82% Infomercial
    15679.9h 1.78% Animationsserie
    13210.9h 1.50% Comedyserie
    12518.9h 1.42% Magazin
    12401.3h 1.41% Morgenmagazin
    11896.6h 1.35% Religionsmagazin
    11718.5h 1.33% Talkshow
    8721.1h  0.99% E-Sport
    8150.2h  0.93% Sitcom
    8103.2h  0.92% Programmende
    7833.8h  0.89% Wetterbericht
    7716.5h  0.88% Börsenmagazin
    7621.9h  0.87% Quiz
    7584.7h  0.86% Komödie
    6509.0h  0.74% Realityshow
    6501.9h  0.74% Wissensmagazin
    6491.8h  0.74% Politikmagazin
    6241.4h  0.71% Wirtschaftsmagazin
    6196.1h  0.70% Telenovela
    5818.1h  0.66% Musikmagazin
