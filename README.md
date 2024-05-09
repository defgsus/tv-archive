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

**108** channels, **846,964.1** hours playtime between **2023-01-17** and **2024-05-10**


### playtime per genre (top 30)

    55278.2h 6.53% Nachrichten
    40424.9h 4.77% Verkaufsshow
    34459.2h 4.07% Krimiserie
    29614.1h 3.50% Werbesendung
    26728.9h 3.16% Dokureihe
    25588.6h 3.02% Dokusoap
    24630.8h 2.91% Regionalmagazin
    21972.3h 2.59% Dokumentation
    21587.7h 2.55% *unknown*
    15576.0h 1.84% Zeichentrickserie
    15387.5h 1.82% Infomercial
    15079.7h 1.78% Animationsserie
    12795.1h 1.51% Comedyserie
    11993.6h 1.42% Magazin
    11934.7h 1.41% Morgenmagazin
    11432.4h 1.35% Religionsmagazin
    11273.3h 1.33% Talkshow
    8403.3h  0.99% E-Sport
    7854.4h  0.93% Programmende
    7812.5h  0.92% Sitcom
    7524.8h  0.89% Wetterbericht
    7465.8h  0.88% Börsenmagazin
    7326.0h  0.86% Quiz
    7289.0h  0.86% Komödie
    6256.2h  0.74% Wissensmagazin
    6239.7h  0.74% Politikmagazin
    6220.5h  0.73% Realityshow
    6050.5h  0.71% Wirtschaftsmagazin
    6033.3h  0.71% Telenovela
    5625.4h  0.66% Musikmagazin
