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

**109** channels, **1,151,707.5** hours playtime between **2023-01-17** and **2024-11-24**


### playtime per genre (top 30)

    75123.6h 6.52% Nachrichten
    52616.7h 4.57% Verkaufsshow
    48048.2h 4.17% Krimiserie
    42401.1h 3.68% Werbesendung
    35913.9h 3.12% Dokureihe
    34307.9h 2.98% Dokusoap
    33706.1h 2.93% Regionalmagazin
    30275.9h 2.63% Dokumentation
    27191.2h 2.36% *unknown*
    21567.2h 1.87% Zeichentrickserie
    21259.5h 1.85% Infomercial
    20580.5h 1.79% Animationsserie
    16483.8h 1.43% Comedyserie
    16111.1h 1.40% Morgenmagazin
    15341.6h 1.33% Religionsmagazin
    15274.4h 1.33% Talkshow
    14374.0h 1.25% Magazin
    11378.5h 0.99% E-Sport
    11135.4h 0.97% Sitcom
    10412.8h 0.90% Wetterbericht
    10177.5h 0.88% Programmende
    10174.2h 0.88% Quiz
    10107.0h 0.88% Komödie
    8833.1h  0.77% Realityshow
    8734.9h  0.76% Politikmagazin
    8653.7h  0.75% Wissensmagazin
    8578.7h  0.74% Börsenmagazin
    7705.1h  0.67% Wirtschaftsmagazin
    7614.5h  0.66% Telenovela
    7574.8h  0.66% Dramaserie
