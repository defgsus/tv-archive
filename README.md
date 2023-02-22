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

**96** channels, **68,336.0** hours playtime between **2023-01-17** and **2023-02-23**


### playtime per genre (top 30)

    4835.9h 7.08% Nachrichten
    3484.6h 5.10% Verkaufsshow
    2897.9h 4.24% Krimiserie
    2327.5h 3.41% Werbesendung
    2290.1h 3.35% Dokusoap
    2001.2h 2.93% Dokureihe
    1999.3h 2.93% Regionalmagazin
    1664.1h 2.44% *unknown*
    1663.6h 2.43% Dokumentation
    1279.8h 1.87% Zeichentrickserie
    1271.5h 1.86% Animationsserie
    1252.4h 1.83% Infomercial
    1133.0h 1.66% Comedyserie
    976.6h  1.43% Morgenmagazin
    913.2h  1.34% Programmende
    892.7h  1.31% Talkshow
    891.0h  1.30% Religionsmagazin
    733.8h  1.07% Magazin
    715.9h  1.05% E-Sport
    647.7h  0.95% Sitcom
    602.4h  0.88% Wetterbericht
    601.4h  0.88% Börsenmagazin
    561.5h  0.82% Wirtschaftsmagazin
    531.3h  0.78% Wissensmagazin
    512.5h  0.75% Quiz
    502.1h  0.73% Musikmagazin
    495.6h  0.73% Dramaserie
    485.4h  0.71% Gesundheitsmagazin
    470.8h  0.69% Telenovela
    447.2h  0.65% Gerichtsshow
