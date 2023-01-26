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

**96** channels, **19,168.5** hours playtime between **2023-01-17** and **2023-01-27**


### playtime per genre (top 30)

    1393.0h 7.27% Nachrichten
    1030.9h 5.38% Verkaufsshow
    819.6h  4.28% Krimiserie
    676.5h  3.53% Dokusoap
    612.1h  3.19% Werbesendung
    579.0h  3.02% Dokureihe
    574.5h  3.00% Regionalmagazin
    490.8h  2.56% Dokumentation
    489.3h  2.55% *unknown*
    380.0h  1.98% Infomercial
    365.6h  1.91% Zeichentrickserie
    342.8h  1.79% Comedyserie
    334.2h  1.74% Animationsserie
    267.8h  1.40% Morgenmagazin
    263.9h  1.38% Talkshow
    241.8h  1.26% Religionsmagazin
    240.8h  1.26% Magazin
    217.3h  1.13% Programmende
    209.2h  1.09% E-Sport
    175.8h  0.92% Sitcom
    170.8h  0.89% Wirtschaftsmagazin
    163.5h  0.85% Tennis
    158.5h  0.83% Wetterbericht
    154.8h  0.81% Wissensmagazin
    150.9h  0.79% Dramaserie
    148.4h  0.77% Börsenmagazin
    147.4h  0.77% Quiz
    145.7h  0.76% Musikmagazin
    144.8h  0.76% Realityshow
    139.3h  0.73% Gesundheitsmagazin
