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

**97** channels, **593,756.7** hours playtime between **2023-01-17** and **2023-12-14**


### playtime per genre (top 30)

    39012.5h 6.57% Nachrichten
    28495.4h 4.80% Verkaufsshow
    23991.8h 4.04% Krimiserie
    20184.1h 3.40% Werbesendung
    19313.3h 3.25% Dokureihe
    17867.5h 3.01% Dokusoap
    17187.4h 2.89% Regionalmagazin
    15193.2h 2.56% Dokumentation
    14525.5h 2.45% *unknown*
    10965.1h 1.85% Zeichentrickserie
    10818.6h 1.82% Infomercial
    10532.9h 1.77% Animationsserie
    9134.7h  1.54% Comedyserie
    8471.9h  1.43% Morgenmagazin
    8041.3h  1.35% Religionsmagazin
    7955.8h  1.34% Talkshow
    7659.7h  1.29% Magazin
    5880.6h  0.99% Programmende
    5837.8h  0.98% E-Sport
    5758.0h  0.97% Sitcom
    5434.8h  0.92% Wetterbericht
    5389.8h  0.91% Börsenmagazin
    4932.6h  0.83% Quiz
    4609.5h  0.78% Komödie
    4527.1h  0.76% Wissensmagazin
    4439.2h  0.75% Wirtschaftsmagazin
    4314.1h  0.73% Telenovela
    4302.6h  0.72% Musikmagazin
    4259.6h  0.72% Realityshow
    4228.5h  0.71% Politikmagazin
