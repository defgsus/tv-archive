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

**108** channels, **852,453.8** hours playtime between **2023-01-17** and **2024-05-14**


### playtime per genre (top 30)

    55634.2h 6.53% Nachrichten
    40628.9h 4.77% Verkaufsshow
    34689.9h 4.07% Krimiserie
    29837.7h 3.50% Werbesendung
    26865.3h 3.15% Dokureihe
    25770.7h 3.02% Dokusoap
    24790.9h 2.91% Regionalmagazin
    22092.8h 2.59% Dokumentation
    21731.9h 2.55% *unknown*
    15677.3h 1.84% Zeichentrickserie
    15506.1h 1.82% Infomercial
    15182.8h 1.78% Animationsserie
    12870.2h 1.51% Comedyserie
    12081.2h 1.42% Magazin
    12008.9h 1.41% Morgenmagazin
    11529.9h 1.35% Religionsmagazin
    11348.5h 1.33% Talkshow
    8461.4h  0.99% E-Sport
    7896.5h  0.93% Programmende
    7862.4h  0.92% Sitcom
    7572.4h  0.89% Wetterbericht
    7492.1h  0.88% Börsenmagazin
    7375.9h  0.87% Quiz
    7303.3h  0.86% Komödie
    6298.1h  0.74% Wissensmagazin
    6265.9h  0.74% Realityshow
    6258.4h  0.73% Politikmagazin
    6078.8h  0.71% Wirtschaftsmagazin
    6061.5h  0.71% Telenovela
    5653.0h  0.66% Musikmagazin
