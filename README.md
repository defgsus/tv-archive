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

**96** channels, **84,749.0** hours playtime between **2023-01-17** and **2023-03-04**


### playtime per genre (top 30)

    6037.4h 7.12% Nachrichten
    4278.6h 5.05% Verkaufsshow
    3610.2h 4.26% Krimiserie
    2871.5h 3.39% Werbesendung
    2803.4h 3.31% Dokusoap
    2527.2h 2.98% Regionalmagazin
    2524.4h 2.98% Dokureihe
    2045.2h 2.41% Dokumentation
    2001.2h 2.36% *unknown*
    1615.4h 1.91% Animationsserie
    1550.5h 1.83% Infomercial
    1547.8h 1.83% Zeichentrickserie
    1386.3h 1.64% Comedyserie
    1232.0h 1.45% Morgenmagazin
    1142.6h 1.35% Programmende
    1114.5h 1.32% Talkshow
    1105.1h 1.30% Religionsmagazin
    903.8h  1.07% Magazin
    879.1h  1.04% E-Sport
    803.2h  0.95% Sitcom
    770.3h  0.91% Börsenmagazin
    750.0h  0.88% Wetterbericht
    692.7h  0.82% Wirtschaftsmagazin
    667.5h  0.79% Wissensmagazin
    638.2h  0.75% Quiz
    622.2h  0.73% Dramaserie
    615.2h  0.73% Musikmagazin
    604.8h  0.71% Gesundheitsmagazin
    591.8h  0.70% Telenovela
    550.2h  0.65% Gerichtsshow
