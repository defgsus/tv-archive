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

**97** channels, **444,865.7** hours playtime between **2023-01-17** and **2023-09-21**


### playtime per genre (top 30)

    29370.0h 6.60% Nachrichten
    21154.2h 4.76% Verkaufsshow
    17988.5h 4.04% Krimiserie
    15009.0h 3.37% Werbesendung
    14656.3h 3.29% Dokureihe
    13519.3h 3.04% Dokusoap
    12823.1h 2.88% Regionalmagazin
    11191.0h 2.52% Dokumentation
    10565.0h 2.37% *unknown*
    8384.7h  1.88% Zeichentrickserie
    8115.9h  1.82% Infomercial
    7895.3h  1.77% Animationsserie
    7211.9h  1.62% Comedyserie
    6296.9h  1.42% Morgenmagazin
    5953.6h  1.34% Religionsmagazin
    5898.9h  1.33% Talkshow
    5555.5h  1.25% Magazin
    4745.0h  1.07% Programmende
    4383.2h  0.99% E-Sport
    4197.6h  0.94% Sitcom
    4189.9h  0.94% Wetterbericht
    4026.9h  0.91% Börsenmagazin
    3701.0h  0.83% Quiz
    3462.0h  0.78% Musikmagazin
    3428.5h  0.77% Komödie
    3369.0h  0.76% Wirtschaftsmagazin
    3332.2h  0.75% Wissensmagazin
    3153.8h  0.71% Telenovela
    2936.2h  0.66% Politikmagazin
    2920.5h  0.66% Reportagereihe
