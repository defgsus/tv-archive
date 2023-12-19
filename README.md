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

**97** channels, **604,507.4** hours playtime between **2023-01-17** and **2023-12-20**


### playtime per genre (top 30)

    39686.0h 6.57% Nachrichten
    29026.3h 4.80% Verkaufsshow
    24420.4h 4.04% Krimiserie
    20548.8h 3.40% Werbesendung
    19658.7h 3.25% Dokureihe
    18162.3h 3.00% Dokusoap
    17494.7h 2.89% Regionalmagazin
    15501.5h 2.56% Dokumentation
    14815.2h 2.45% *unknown*
    11169.7h 1.85% Zeichentrickserie
    11013.5h 1.82% Infomercial
    10703.4h 1.77% Animationsserie
    9262.0h  1.53% Comedyserie
    8621.9h  1.43% Morgenmagazin
    8192.7h  1.36% Religionsmagazin
    8097.0h  1.34% Talkshow
    7798.8h  1.29% Magazin
    5962.6h  0.99% Programmende
    5948.1h  0.98% E-Sport
    5856.1h  0.97% Sitcom
    5528.8h  0.91% Wetterbericht
    5466.0h  0.90% Börsenmagazin
    5007.7h  0.83% Quiz
    4737.3h  0.78% Komödie
    4608.8h  0.76% Wissensmagazin
    4505.6h  0.75% Wirtschaftsmagazin
    4390.1h  0.73% Telenovela
    4369.9h  0.72% Musikmagazin
    4365.6h  0.72% Realityshow
    4296.6h  0.71% Politikmagazin
