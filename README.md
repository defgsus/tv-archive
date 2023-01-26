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

**96** channels, **19,172.1** hours playtime between **2023-01-17** and **2023-01-27**


### playtime per genre (top 30)

    1392.9h 7.27% Nachrichten
    1034.6h 5.40% Verkaufsshow
    819.5h  4.27% Krimiserie
    676.8h  3.53% Dokusoap
    612.1h  3.19% Werbesendung
    578.4h  3.02% Dokureihe
    574.3h  3.00% Regionalmagazin
    491.5h  2.56% Dokumentation
    490.3h  2.56% *unknown*
    380.0h  1.98% Infomercial
    366.1h  1.91% Zeichentrickserie
    340.6h  1.78% Comedyserie
    333.8h  1.74% Animationsserie
    267.8h  1.40% Morgenmagazin
    264.0h  1.38% Talkshow
    241.8h  1.26% Religionsmagazin
    241.7h  1.26% Magazin
    217.3h  1.13% Programmende
    209.9h  1.09% E-Sport
    175.8h  0.92% Sitcom
    170.8h  0.89% Wirtschaftsmagazin
    163.5h  0.85% Tennis
    158.4h  0.83% Wetterbericht
    154.9h  0.81% Wissensmagazin
    150.5h  0.79% Dramaserie
    148.0h  0.77% Börsenmagazin
    147.3h  0.77% Quiz
    145.0h  0.76% Realityshow
    145.0h  0.76% Musikmagazin
    139.3h  0.73% Gesundheitsmagazin
