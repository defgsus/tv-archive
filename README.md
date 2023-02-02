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

**96** channels, **31,930.5** hours playtime between **2023-01-17** and **2023-02-03**


### playtime per genre (top 30)

    2271.4h 7.11% Nachrichten
    1691.2h 5.30% Verkaufsshow
    1359.2h 4.26% Krimiserie
    1138.4h 3.57% Dokusoap
    1060.2h 3.32% Werbesendung
    959.2h  3.00% Dokureihe
    945.3h  2.96% Regionalmagazin
    817.3h  2.56% Dokumentation
    777.7h  2.44% *unknown*
    621.0h  1.94% Zeichentrickserie
    608.3h  1.91% Infomercial
    564.0h  1.77% Animationsserie
    558.8h  1.75% Comedyserie
    454.2h  1.42% Morgenmagazin
    416.6h  1.30% Religionsmagazin
    409.5h  1.28% Talkshow
    405.1h  1.27% Programmende
    368.5h  1.15% Magazin
    347.7h  1.09% E-Sport
    295.0h  0.92% Sitcom
    276.4h  0.87% Börsenmagazin
    272.5h  0.85% Wirtschaftsmagazin
    271.4h  0.85% Wetterbericht
    260.4h  0.82% Wissensmagazin
    253.0h  0.79% Quiz
    247.3h  0.77% Dramaserie
    241.2h  0.76% Musikmagazin
    232.9h  0.73% Telenovela
    230.9h  0.72% Gesundheitsmagazin
    220.1h  0.69% Realityshow
