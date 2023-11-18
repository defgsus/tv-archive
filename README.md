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

**97** channels, **550,647.2** hours playtime between **2023-01-17** and **2023-11-19**


### playtime per genre (top 30)

    36240.5h 6.58% Nachrichten
    26319.0h 4.78% Verkaufsshow
    22205.2h 4.03% Krimiserie
    18687.7h 3.39% Werbesendung
    17980.4h 3.27% Dokureihe
    16668.3h 3.03% Dokusoap
    15907.7h 2.89% Regionalmagazin
    14043.7h 2.55% Dokumentation
    13386.3h 2.43% *unknown*
    10211.7h 1.85% Zeichentrickserie
    10037.9h 1.82% Infomercial
    9825.1h  1.78% Animationsserie
    8641.5h  1.57% Comedyserie
    7837.7h  1.42% Morgenmagazin
    7431.4h  1.35% Religionsmagazin
    7353.0h  1.34% Talkshow
    7021.8h  1.28% Magazin
    5554.4h  1.01% Programmende
    5385.7h  0.98% E-Sport
    5283.5h  0.96% Sitcom
    5063.8h  0.92% Wetterbericht
    4990.6h  0.91% Börsenmagazin
    4597.9h  0.84% Quiz
    4303.8h  0.78% Komödie
    4175.2h  0.76% Wissensmagazin
    4135.7h  0.75% Wirtschaftsmagazin
    4061.7h  0.74% Musikmagazin
    3978.2h  0.72% Telenovela
    3847.4h  0.70% Politikmagazin
    3801.7h  0.69% Realityshow
