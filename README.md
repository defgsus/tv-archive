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

**97** channels, **441,324.1** hours playtime between **2023-01-17** and **2023-09-19**


### playtime per genre (top 30)

    29113.7h 6.60% Nachrichten
    20962.8h 4.75% Verkaufsshow
    17845.8h 4.04% Krimiserie
    14893.6h 3.37% Werbesendung
    14540.3h 3.29% Dokureihe
    13412.7h 3.04% Dokusoap
    12701.2h 2.88% Regionalmagazin
    11117.1h 2.52% Dokumentation
    10477.5h 2.37% *unknown*
    8324.2h  1.89% Zeichentrickserie
    8050.1h  1.82% Infomercial
    7829.0h  1.77% Animationsserie
    7144.4h  1.62% Comedyserie
    6233.4h  1.41% Morgenmagazin
    5908.7h  1.34% Religionsmagazin
    5851.2h  1.33% Talkshow
    5518.4h  1.25% Magazin
    4715.5h  1.07% Programmende
    4357.8h  0.99% E-Sport
    4159.7h  0.94% Wetterbericht
    4153.1h  0.94% Sitcom
    3984.6h  0.90% Börsenmagazin
    3667.3h  0.83% Quiz
    3444.8h  0.78% Musikmagazin
    3417.9h  0.77% Komödie
    3337.2h  0.76% Wirtschaftsmagazin
    3300.5h  0.75% Wissensmagazin
    3114.0h  0.71% Telenovela
    2909.8h  0.66% Reportagereihe
    2886.3h  0.65% Politikmagazin
