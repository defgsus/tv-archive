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

**97** channels, **545,271.3** hours playtime between **2023-01-17** and **2023-11-16**


### playtime per genre (top 30)

    35895.8h 6.58% Nachrichten
    26048.2h 4.78% Verkaufsshow
    21957.8h 4.03% Krimiserie
    18496.2h 3.39% Werbesendung
    17820.9h 3.27% Dokureihe
    16541.4h 3.03% Dokusoap
    15760.7h 2.89% Regionalmagazin
    13911.0h 2.55% Dokumentation
    13238.7h 2.43% *unknown*
    10111.5h 1.85% Zeichentrickserie
    9937.3h  1.82% Infomercial
    9739.5h  1.79% Animationsserie
    8567.7h  1.57% Comedyserie
    7763.2h  1.42% Morgenmagazin
    7354.7h  1.35% Religionsmagazin
    7290.1h  1.34% Talkshow
    6953.1h  1.28% Magazin
    5513.0h  1.01% Programmende
    5343.7h  0.98% E-Sport
    5238.8h  0.96% Sitcom
    5019.7h  0.92% Wetterbericht
    4943.7h  0.91% Börsenmagazin
    4552.4h  0.83% Quiz
    4246.4h  0.78% Komödie
    4134.6h  0.76% Wissensmagazin
    4101.5h  0.75% Wirtschaftsmagazin
    4030.5h  0.74% Musikmagazin
    3937.6h  0.72% Telenovela
    3799.9h  0.70% Politikmagazin
    3736.5h  0.69% Realityshow
