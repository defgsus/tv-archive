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

**110** channels, **1,236,045.6** hours playtime between **2023-01-17** and **2025-01-20**


### playtime per genre (top 30)

    80878.6h 6.54% Nachrichten
    55828.8h 4.52% Verkaufsshow
    51231.0h 4.14% Krimiserie
    45944.2h 3.72% Werbesendung
    38442.8h 3.11% Dokureihe
    36315.3h 2.94% Dokusoap
    35946.9h 2.91% Regionalmagazin
    32983.1h 2.67% Dokumentation
    29461.2h 2.38% *unknown*
    23274.2h 1.88% Zeichentrickserie
    22894.3h 1.85% Infomercial
    22099.5h 1.79% Animationsserie
    17327.1h 1.40% Comedyserie
    17236.8h 1.39% Morgenmagazin
    16311.0h 1.32% Talkshow
    16123.4h 1.30% Religionsmagazin
    14990.9h 1.21% Magazin
    12250.6h 0.99% E-Sport
    11831.9h 0.96% Sitcom
    11324.9h 0.92% Komödie
    11195.2h 0.91% Wetterbericht
    10957.6h 0.89% Quiz
    10838.5h 0.88% Programmende
    9574.8h  0.77% Realityshow
    9413.4h  0.76% Politikmagazin
    9145.4h  0.74% Wissensmagazin
    8813.6h  0.71% Börsenmagazin
    8189.6h  0.66% Dramaserie
    8178.0h  0.66% Arztserie
    8167.5h  0.66% Wirtschaftsmagazin
