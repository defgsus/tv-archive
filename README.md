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

**97** channels, **590,157.9** hours playtime between **2023-01-17** and **2023-12-12**


### playtime per genre (top 30)

    38757.3h 6.57% Nachrichten
    28311.7h 4.80% Verkaufsshow
    23822.7h 4.04% Krimiserie
    20059.8h 3.40% Werbesendung
    19201.4h 3.25% Dokureihe
    17776.8h 3.01% Dokusoap
    17058.3h 2.89% Regionalmagazin
    15108.3h 2.56% Dokumentation
    14442.7h 2.45% *unknown*
    10903.8h 1.85% Zeichentrickserie
    10753.7h 1.82% Infomercial
    10474.6h 1.77% Animationsserie
    9089.3h  1.54% Comedyserie
    8403.4h  1.42% Morgenmagazin
    7995.2h  1.35% Religionsmagazin
    7915.1h  1.34% Talkshow
    7601.1h  1.29% Magazin
    5852.2h  0.99% Programmende
    5791.7h  0.98% E-Sport
    5701.6h  0.97% Sitcom
    5402.8h  0.92% Wetterbericht
    5349.2h  0.91% Börsenmagazin
    4901.1h  0.83% Quiz
    4595.0h  0.78% Komödie
    4497.0h  0.76% Wissensmagazin
    4411.2h  0.75% Wirtschaftsmagazin
    4285.5h  0.73% Musikmagazin
    4273.5h  0.72% Telenovela
    4223.3h  0.72% Realityshow
    4186.8h  0.71% Politikmagazin
