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

**109** channels, **1,170,095.6** hours playtime between **2023-01-17** and **2024-12-07**


### playtime per genre (top 30)

    76478.7h 6.54% Nachrichten
    53273.7h 4.55% Verkaufsshow
    48832.3h 4.17% Krimiserie
    43134.5h 3.69% Werbesendung
    36460.9h 3.12% Dokureihe
    34748.5h 2.97% Dokusoap
    34278.4h 2.93% Regionalmagazin
    30796.9h 2.63% Dokumentation
    27560.8h 2.36% *unknown*
    21927.2h 1.87% Zeichentrickserie
    21641.4h 1.85% Infomercial
    20922.8h 1.79% Animationsserie
    16674.4h 1.43% Comedyserie
    16403.0h 1.40% Morgenmagazin
    15526.9h 1.33% Talkshow
    15519.8h 1.33% Religionsmagazin
    14510.5h 1.24% Magazin
    11558.7h 0.99% E-Sport
    11287.7h 0.96% Sitcom
    10575.5h 0.90% Wetterbericht
    10354.8h 0.88% Quiz
    10329.3h 0.88% Programmende
    10276.3h 0.88% Komödie
    9013.1h  0.77% Realityshow
    8924.4h  0.76% Politikmagazin
    8775.5h  0.75% Wissensmagazin
    8647.1h  0.74% Börsenmagazin
    7828.1h  0.67% Wirtschaftsmagazin
    7766.1h  0.66% Telenovela
    7747.2h  0.66% Dramaserie
