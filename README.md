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

**109** channels, **1,170,013.1** hours playtime between **2023-01-17** and **2024-12-06**


### playtime per genre (top 30)

    76478.5h 6.54% Nachrichten
    53281.5h 4.55% Verkaufsshow
    48830.8h 4.17% Krimiserie
    43147.0h 3.69% Werbesendung
    36456.8h 3.12% Dokureihe
    34746.7h 2.97% Dokusoap
    34279.7h 2.93% Regionalmagazin
    30794.0h 2.63% Dokumentation
    27545.0h 2.35% *unknown*
    21928.0h 1.87% Zeichentrickserie
    21643.4h 1.85% Infomercial
    20920.5h 1.79% Animationsserie
    16665.7h 1.42% Comedyserie
    16400.3h 1.40% Morgenmagazin
    15520.1h 1.33% Talkshow
    15517.5h 1.33% Religionsmagazin
    14510.2h 1.24% Magazin
    11556.3h 0.99% E-Sport
    11287.7h 0.96% Sitcom
    10575.1h 0.90% Wetterbericht
    10360.8h 0.89% Quiz
    10328.8h 0.88% Programmende
    10265.5h 0.88% Komödie
    9028.1h  0.77% Realityshow
    8933.5h  0.76% Politikmagazin
    8780.2h  0.75% Wissensmagazin
    8647.1h  0.74% Börsenmagazin
    7830.2h  0.67% Wirtschaftsmagazin
    7756.5h  0.66% Telenovela
    7748.1h  0.66% Dramaserie
