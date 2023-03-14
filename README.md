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

**96** channels, **104,667.9** hours playtime between **2023-01-17** and **2023-03-15**


### playtime per genre (top 30)

    7362.7h 7.03% Nachrichten
    5254.6h 5.02% Verkaufsshow
    4394.2h 4.20% Krimiserie
    3554.1h 3.40% Werbesendung
    3361.5h 3.21% Dokusoap
    3176.0h 3.03% Dokureihe
    3078.0h 2.94% Regionalmagazin
    2574.0h 2.46% Dokumentation
    2480.6h 2.37% *unknown*
    2006.5h 1.92% Animationsserie
    1919.7h 1.83% Infomercial
    1888.6h 1.80% Zeichentrickserie
    1699.9h 1.62% Comedyserie
    1487.0h 1.42% Morgenmagazin
    1418.0h 1.35% Programmende
    1387.5h 1.33% Talkshow
    1373.1h 1.31% Religionsmagazin
    1085.7h 1.04% Magazin
    1080.6h 1.03% E-Sport
    995.9h  0.95% Sitcom
    978.7h  0.94% Börsenmagazin
    927.5h  0.89% Wetterbericht
    851.2h  0.81% Wirtschaftsmagazin
    819.3h  0.78% Wissensmagazin
    786.1h  0.75% Quiz
    774.7h  0.74% Musikmagazin
    754.1h  0.72% Dramaserie
    733.2h  0.70% Telenovela
    723.7h  0.69% Gesundheitsmagazin
    679.3h  0.65% Sportmagazin
