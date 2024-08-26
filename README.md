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

**109** channels, **1,016,122.9** hours playtime between **2023-01-17** and **2024-08-27**


### playtime per genre (top 30)

    66090.1h 6.50% Nachrichten
    47280.5h 4.65% Verkaufsshow
    41772.8h 4.11% Krimiserie
    36654.8h 3.61% Werbesendung
    31949.8h 3.14% Dokureihe
    30711.3h 3.02% Dokusoap
    29603.3h 2.91% Regionalmagazin
    26540.1h 2.61% Dokumentation
    24761.1h 2.44% *unknown*
    18853.5h 1.86% Zeichentrickserie
    18613.6h 1.83% Infomercial
    18205.5h 1.79% Animationsserie
    14901.2h 1.47% Comedyserie
    14237.0h 1.40% Morgenmagazin
    13819.0h 1.36% Religionsmagazin
    13550.0h 1.33% Magazin
    13336.8h 1.31% Talkshow
    10039.5h 0.99% E-Sport
    9686.1h  0.95% Sitcom
    9181.0h  0.90% Wetterbericht
    9138.4h  0.90% Programmende
    8937.2h  0.88% Komödie
    8763.8h  0.86% Quiz
    8154.8h  0.80% Börsenmagazin
    7587.9h  0.75% Politikmagazin
    7581.3h  0.75% Wissensmagazin
    7524.4h  0.74% Realityshow
    6925.9h  0.68% Wirtschaftsmagazin
    6672.0h  0.66% Telenovela
    6629.8h  0.65% Dramaserie
