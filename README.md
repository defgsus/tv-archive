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

**109** channels, **1,159,948.1** hours playtime between **2023-01-17** and **2024-11-29**


### playtime per genre (top 30)

    75758.9h 6.53% Nachrichten
    52955.5h 4.57% Verkaufsshow
    48419.7h 4.17% Krimiserie
    42726.2h 3.68% Werbesendung
    36163.2h 3.12% Dokureihe
    34508.9h 2.98% Dokusoap
    33975.9h 2.93% Regionalmagazin
    30493.8h 2.63% Dokumentation
    27328.8h 2.36% *unknown*
    21731.7h 1.87% Zeichentrickserie
    21428.2h 1.85% Infomercial
    20729.0h 1.79% Animationsserie
    16562.0h 1.43% Comedyserie
    16254.5h 1.40% Morgenmagazin
    15422.6h 1.33% Religionsmagazin
    15397.8h 1.33% Talkshow
    14430.9h 1.24% Magazin
    11456.1h 0.99% E-Sport
    11200.6h 0.97% Sitcom
    10478.8h 0.90% Wetterbericht
    10268.9h 0.89% Quiz
    10245.4h 0.88% Programmende
    10155.4h 0.88% Komödie
    8934.7h  0.77% Realityshow
    8835.1h  0.76% Politikmagazin
    8714.2h  0.75% Wissensmagazin
    8611.7h  0.74% Börsenmagazin
    7766.1h  0.67% Wirtschaftsmagazin
    7688.6h  0.66% Telenovela
    7679.8h  0.66% Dramaserie
