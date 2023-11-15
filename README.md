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

**97** channels, **545,270.4** hours playtime between **2023-01-17** and **2023-11-16**


### playtime per genre (top 30)

    35897.0h 6.58% Nachrichten
    26050.2h 4.78% Verkaufsshow
    21957.8h 4.03% Krimiserie
    18494.2h 3.39% Werbesendung
    17821.0h 3.27% Dokureihe
    16541.3h 3.03% Dokusoap
    15761.0h 2.89% Regionalmagazin
    13910.5h 2.55% Dokumentation
    13239.9h 2.43% *unknown*
    10112.3h 1.85% Zeichentrickserie
    9937.3h  1.82% Infomercial
    9738.9h  1.79% Animationsserie
    8567.9h  1.57% Comedyserie
    7763.2h  1.42% Morgenmagazin
    7354.1h  1.35% Religionsmagazin
    7290.9h  1.34% Talkshow
    6953.1h  1.28% Magazin
    5513.1h  1.01% Programmende
    5343.7h  0.98% E-Sport
    5238.9h  0.96% Sitcom
    5019.8h  0.92% Wetterbericht
    4944.0h  0.91% Börsenmagazin
    4552.4h  0.83% Quiz
    4246.4h  0.78% Komödie
    4134.5h  0.76% Wissensmagazin
    4101.5h  0.75% Wirtschaftsmagazin
    4030.5h  0.74% Musikmagazin
    3936.9h  0.72% Telenovela
    3795.0h  0.70% Politikmagazin
    3736.5h  0.69% Realityshow
