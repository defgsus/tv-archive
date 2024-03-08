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

**99** channels, **746,586.5** hours playtime between **2023-01-17** and **2024-03-09**


### playtime per genre (top 30)

    48622.6h 6.51% Nachrichten
    35871.0h 4.80% Verkaufsshow
    30399.9h 4.07% Krimiserie
    25843.0h 3.46% Werbesendung
    23841.9h 3.19% Dokureihe
    22561.7h 3.02% Dokusoap
    21693.5h 2.91% Regionalmagazin
    19209.3h 2.57% Dokumentation
    19157.2h 2.57% *unknown*
    13806.1h 1.85% Zeichentrickserie
    13575.7h 1.82% Infomercial
    13169.1h 1.76% Animationsserie
    11341.1h 1.52% Comedyserie
    10613.4h 1.42% Morgenmagazin
    10089.2h 1.35% Magazin
    10084.0h 1.35% Religionsmagazin
    9940.0h  1.33% Talkshow
    7377.5h  0.99% E-Sport
    7069.3h  0.95% Programmende
    7029.9h  0.94% Sitcom
    6655.6h  0.89% Börsenmagazin
    6634.9h  0.89% Wetterbericht
    6325.7h  0.85% Quiz
    6324.7h  0.85% Komödie
    5580.1h  0.75% Wissensmagazin
    5423.5h  0.73% Realityshow
    5414.7h  0.73% Wirtschaftsmagazin
    5393.5h  0.72% Politikmagazin
    5342.9h  0.72% Telenovela
    5105.1h  0.68% Musikmagazin
