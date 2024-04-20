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

**102** channels, **819,376.5** hours playtime between **2023-01-17** and **2024-04-21**


### playtime per genre (top 30)

    53371.6h 6.51% Nachrichten
    39322.3h 4.80% Verkaufsshow
    33370.8h 4.07% Krimiserie
    28615.4h 3.49% Werbesendung
    25947.4h 3.17% Dokureihe
    24717.8h 3.02% Dokusoap
    23831.2h 2.91% Regionalmagazin
    21187.1h 2.59% Dokumentation
    20982.7h 2.56% *unknown*
    15035.4h 1.83% Zeichentrickserie
    14878.7h 1.82% Infomercial
    14583.0h 1.78% Animationsserie
    12421.0h 1.52% Comedyserie
    11567.2h 1.41% Morgenmagazin
    11444.5h 1.40% Magazin
    11047.2h 1.35% Religionsmagazin
    10904.4h 1.33% Talkshow
    8099.8h  0.99% E-Sport
    7634.6h  0.93% Programmende
    7551.6h  0.92% Sitcom
    7270.8h  0.89% Wetterbericht
    7208.1h  0.88% Börsenmagazin
    7066.2h  0.86% Quiz
    7001.5h  0.85% Komödie
    6074.9h  0.74% Wissensmagazin
    5975.6h  0.73% Politikmagazin
    5907.4h  0.72% Realityshow
    5867.0h  0.72% Wirtschaftsmagazin
    5864.6h  0.72% Telenovela
    5474.0h  0.67% Musikmagazin
