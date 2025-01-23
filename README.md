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

**110** channels, **1,242,998.6** hours playtime between **2023-01-17** and **2025-01-24**


### playtime per genre (top 30)

    81418.8h 6.55% Nachrichten
    56090.4h 4.51% Verkaufsshow
    51570.7h 4.15% Krimiserie
    46240.2h 3.72% Werbesendung
    38642.1h 3.11% Dokureihe
    36509.2h 2.94% Dokusoap
    36195.0h 2.91% Regionalmagazin
    33172.2h 2.67% Dokumentation
    29632.9h 2.38% *unknown*
    23416.3h 1.88% Zeichentrickserie
    23026.8h 1.85% Infomercial
    22221.4h 1.79% Animationsserie
    17413.4h 1.40% Comedyserie
    17371.5h 1.40% Morgenmagazin
    16387.6h 1.32% Talkshow
    16170.6h 1.30% Religionsmagazin
    15028.0h 1.21% Magazin
    12323.8h 0.99% E-Sport
    11910.2h 0.96% Sitcom
    11353.1h 0.91% Komödie
    11264.3h 0.91% Wetterbericht
    11063.7h 0.89% Quiz
    10893.5h 0.88% Programmende
    9642.7h  0.78% Realityshow
    9501.9h  0.76% Politikmagazin
    9174.0h  0.74% Wissensmagazin
    8844.1h  0.71% Börsenmagazin
    8260.6h  0.66% Dramaserie
    8241.9h  0.66% Arztserie
    8220.5h  0.66% Wirtschaftsmagazin
