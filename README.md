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

**109** channels, **1,210,075.0** hours playtime between **2023-01-17** and **2025-01-02**


### playtime per genre (top 30)

    79054.6h 6.53% Nachrichten
    54887.2h 4.54% Verkaufsshow
    50164.4h 4.15% Krimiserie
    44821.5h 3.70% Werbesendung
    37656.9h 3.11% Dokureihe
    35611.3h 2.94% Dokusoap
    35243.1h 2.91% Regionalmagazin
    32198.0h 2.66% Dokumentation
    28750.1h 2.38% *unknown*
    22731.4h 1.88% Zeichentrickserie
    22385.0h 1.85% Infomercial
    21607.1h 1.79% Animationsserie
    17072.3h 1.41% Comedyserie
    16876.8h 1.39% Morgenmagazin
    15969.1h 1.32% Talkshow
    15873.9h 1.31% Religionsmagazin
    14797.4h 1.22% Magazin
    11964.8h 0.99% E-Sport
    11586.6h 0.96% Sitcom
    11085.3h 0.92% Komödie
    10944.6h 0.90% Wetterbericht
    10701.0h 0.88% Quiz
    10639.0h 0.88% Programmende
    9342.7h  0.77% Realityshow
    9214.6h  0.76% Politikmagazin
    9000.4h  0.74% Wissensmagazin
    8736.3h  0.72% Börsenmagazin
    8014.2h  0.66% Wirtschaftsmagazin
    8005.1h  0.66% Arztserie
    7995.6h  0.66% Dramaserie
