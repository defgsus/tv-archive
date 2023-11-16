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

**97** channels, **547,059.2** hours playtime between **2023-01-17** and **2023-11-17**


### playtime per genre (top 30)

    36032.6h 6.59% Nachrichten
    26142.2h 4.78% Verkaufsshow
    22052.8h 4.03% Krimiserie
    18551.2h 3.39% Werbesendung
    17871.5h 3.27% Dokureihe
    16605.7h 3.04% Dokusoap
    15824.9h 2.89% Regionalmagazin
    13957.9h 2.55% Dokumentation
    13281.1h 2.43% *unknown*
    10139.1h 1.85% Zeichentrickserie
    9969.9h  1.82% Infomercial
    9772.6h  1.79% Animationsserie
    8587.0h  1.57% Comedyserie
    7797.4h  1.43% Morgenmagazin
    7377.3h  1.35% Religionsmagazin
    7310.3h  1.34% Talkshow
    6979.8h  1.28% Magazin
    5525.7h  1.01% Programmende
    5352.5h  0.98% E-Sport
    5253.1h  0.96% Sitcom
    5035.8h  0.92% Wetterbericht
    4955.1h  0.91% Börsenmagazin
    4570.9h  0.84% Quiz
    4259.7h  0.78% Komödie
    4147.9h  0.76% Wissensmagazin
    4118.5h  0.75% Wirtschaftsmagazin
    4042.8h  0.74% Musikmagazin
    3956.4h  0.72% Telenovela
    3822.0h  0.70% Politikmagazin
    3766.0h  0.69% Realityshow
