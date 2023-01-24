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

**96** channels, **15,437.7** hours playtime between **2023-01-17** and **2023-01-25**


### playtime per genre (top 30)

    1097.3h 7.11% Nachrichten
    841.7h  5.45% Verkaufsshow
    661.3h  4.28% Krimiserie
    518.1h  3.36% Dokusoap
    498.7h  3.23% Werbesendung
    490.7h  3.18% Dokureihe
    422.6h  2.74% Regionalmagazin
    405.9h  2.63% *unknown*
    383.1h  2.48% Dokumentation
    309.2h  2.00% Infomercial
    295.5h  1.91% Zeichentrickserie
    267.8h  1.73% Animationsserie
    267.1h  1.73% Comedyserie
    209.6h  1.36% Talkshow
    204.6h  1.33% Religionsmagazin
    198.8h  1.29% Morgenmagazin
    195.5h  1.27% Magazin
    173.8h  1.13% E-Sport
    147.1h  0.95% Programmende
    135.9h  0.88% Wirtschaftsmagazin
    132.5h  0.86% Sitcom
    127.8h  0.83% Dramaserie
    125.3h  0.81% Wetterbericht
    124.1h  0.80% Tennis
    123.2h  0.80% Wissensmagazin
    122.9h  0.80% Börsenmagazin
    116.3h  0.75% Realityshow
    116.2h  0.75% Musikmagazin
    114.2h  0.74% Quiz
    111.8h  0.72% Krankenhausserie
