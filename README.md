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

**109** channels, **1,150,365.8** hours playtime between **2023-01-17** and **2024-11-22**


### playtime per genre (top 30)

    75045.1h 6.52% Nachrichten
    52551.7h 4.57% Verkaufsshow
    48026.1h 4.17% Krimiserie
    42357.0h 3.68% Werbesendung
    35874.1h 3.12% Dokureihe
    34276.6h 2.98% Dokusoap
    33689.9h 2.93% Regionalmagazin
    30229.2h 2.63% Dokumentation
    27135.5h 2.36% *unknown*
    21530.1h 1.87% Zeichentrickserie
    21223.9h 1.84% Infomercial
    20548.2h 1.79% Animationsserie
    16478.8h 1.43% Comedyserie
    16097.4h 1.40% Morgenmagazin
    15322.6h 1.33% Religionsmagazin
    15237.7h 1.32% Talkshow
    14360.7h 1.25% Magazin
    11364.1h 0.99% E-Sport
    11145.8h 0.97% Sitcom
    10412.4h 0.91% Wetterbericht
    10186.8h 0.89% Quiz
    10162.0h 0.88% Programmende
    10093.7h 0.88% Komödie
    8849.1h  0.77% Realityshow
    8741.1h  0.76% Politikmagazin
    8652.4h  0.75% Wissensmagazin
    8578.9h  0.75% Börsenmagazin
    7706.0h  0.67% Wirtschaftsmagazin
    7616.0h  0.66% Telenovela
    7593.3h  0.66% Dramaserie
