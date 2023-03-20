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

**96** channels, **115,548.3** hours playtime between **2023-01-17** and **2023-03-21**


### playtime per genre (top 30)

    8095.7h 7.01% Nachrichten
    5791.5h 5.01% Verkaufsshow
    4809.6h 4.16% Krimiserie
    3906.2h 3.38% Werbesendung
    3659.8h 3.17% Dokusoap
    3548.3h 3.07% Dokureihe
    3390.0h 2.93% Regionalmagazin
    2833.2h 2.45% Dokumentation
    2713.9h 2.35% *unknown*
    2203.8h 1.91% Animationsserie
    2121.9h 1.84% Infomercial
    2090.0h 1.81% Zeichentrickserie
    1883.0h 1.63% Comedyserie
    1637.5h 1.42% Morgenmagazin
    1585.1h 1.37% Programmende
    1532.5h 1.33% Talkshow
    1505.7h 1.30% Religionsmagazin
    1207.2h 1.04% Magazin
    1195.3h 1.03% E-Sport
    1098.2h 0.95% Sitcom
    1070.7h 0.93% Börsenmagazin
    1029.1h 0.89% Wetterbericht
    941.9h  0.82% Wirtschaftsmagazin
    907.3h  0.79% Wissensmagazin
    870.8h  0.75% Quiz
    863.5h  0.75% Musikmagazin
    839.4h  0.73% Dramaserie
    799.2h  0.69% Telenovela
    794.7h  0.69% Gesundheitsmagazin
    786.2h  0.68% Sportmagazin
