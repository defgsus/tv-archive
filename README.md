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

**96** channels, **92,037.6** hours playtime between **2023-01-17** and **2023-03-08**


### playtime per genre (top 30)

    6498.1h 7.06% Nachrichten
    4616.8h 5.02% Verkaufsshow
    3873.3h 4.21% Krimiserie
    3125.0h 3.40% Werbesendung
    3010.7h 3.27% Dokusoap
    2754.2h 2.99% Dokureihe
    2704.2h 2.94% Regionalmagazin
    2267.8h 2.46% Dokumentation
    2222.6h 2.41% *unknown*
    1757.4h 1.91% Animationsserie
    1684.2h 1.83% Infomercial
    1666.4h 1.81% Zeichentrickserie
    1487.8h 1.62% Comedyserie
    1300.8h 1.41% Morgenmagazin
    1240.6h 1.35% Programmende
    1212.9h 1.32% Religionsmagazin
    1208.8h 1.31% Talkshow
    963.9h  1.05% Magazin
    959.7h  1.04% E-Sport
    868.2h  0.94% Sitcom
    844.9h  0.92% Börsenmagazin
    809.5h  0.88% Wetterbericht
    746.0h  0.81% Wirtschaftsmagazin
    722.4h  0.78% Wissensmagazin
    687.5h  0.75% Quiz
    676.7h  0.74% Musikmagazin
    662.8h  0.72% Dramaserie
    648.2h  0.70% Gesundheitsmagazin
    633.1h  0.69% Telenovela
    596.5h  0.65% Sportmagazin
