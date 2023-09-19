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

**97** channels, **443,102.0** hours playtime between **2023-01-17** and **2023-09-20**


### playtime per genre (top 30)

    29240.9h 6.60% Nachrichten
    21054.4h 4.75% Verkaufsshow
    17936.7h 4.05% Krimiserie
    14951.7h 3.37% Werbesendung
    14594.2h 3.29% Dokureihe
    13473.8h 3.04% Dokusoap
    12761.3h 2.88% Regionalmagazin
    11154.8h 2.52% Dokumentation
    10518.0h 2.37% *unknown*
    8355.6h  1.89% Zeichentrickserie
    8082.9h  1.82% Infomercial
    7862.5h  1.77% Animationsserie
    7176.8h  1.62% Comedyserie
    6265.2h  1.41% Morgenmagazin
    5932.1h  1.34% Religionsmagazin
    5871.5h  1.33% Talkshow
    5537.3h  1.25% Magazin
    4730.4h  1.07% Programmende
    4371.2h  0.99% E-Sport
    4173.9h  0.94% Wetterbericht
    4169.6h  0.94% Sitcom
    4012.9h  0.91% Börsenmagazin
    3682.0h  0.83% Quiz
    3455.6h  0.78% Musikmagazin
    3419.7h  0.77% Komödie
    3351.2h  0.76% Wirtschaftsmagazin
    3314.3h  0.75% Wissensmagazin
    3133.8h  0.71% Telenovela
    2909.7h  0.66% Politikmagazin
    2907.7h  0.66% Reportagereihe
