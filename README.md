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

**110** channels, **1,222,170.8** hours playtime between **2023-01-17** and **2025-01-10**


### playtime per genre (top 30)

    79932.7h 6.54% Nachrichten
    55287.8h 4.52% Verkaufsshow
    50692.6h 4.15% Krimiserie
    45340.4h 3.71% Werbesendung
    38060.3h 3.11% Dokureihe
    35940.3h 2.94% Dokusoap
    35596.6h 2.91% Regionalmagazin
    32565.2h 2.66% Dokumentation
    29081.0h 2.38% *unknown*
    22989.1h 1.88% Zeichentrickserie
    22624.9h 1.85% Infomercial
    21838.4h 1.79% Animationsserie
    17189.3h 1.41% Comedyserie
    17065.3h 1.40% Morgenmagazin
    16096.6h 1.32% Talkshow
    15979.3h 1.31% Religionsmagazin
    14906.6h 1.22% Magazin
    12099.8h 0.99% E-Sport
    11706.9h 0.96% Sitcom
    11201.4h 0.92% Komödie
    11068.2h 0.91% Wetterbericht
    10844.7h 0.89% Quiz
    10735.0h 0.88% Programmende
    9463.0h  0.77% Realityshow
    9312.5h  0.76% Politikmagazin
    9067.8h  0.74% Wissensmagazin
    8780.6h  0.72% Börsenmagazin
    8100.2h  0.66% Dramaserie
    8095.4h  0.66% Wirtschaftsmagazin
    8088.0h  0.66% Arztserie
