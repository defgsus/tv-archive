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

**96** channels, **68,354.7** hours playtime between **2023-01-17** and **2023-02-23**


### playtime per genre (top 30)

    4840.1h 7.08% Nachrichten
    3484.8h 5.10% Verkaufsshow
    2897.5h 4.24% Krimiserie
    2329.5h 3.41% Werbesendung
    2290.1h 3.35% Dokusoap
    2001.8h 2.93% Dokureihe
    2001.6h 2.93% Regionalmagazin
    1667.5h 2.44% *unknown*
    1664.5h 2.44% Dokumentation
    1279.7h 1.87% Zeichentrickserie
    1271.3h 1.86% Animationsserie
    1252.9h 1.83% Infomercial
    1133.3h 1.66% Comedyserie
    976.6h  1.43% Morgenmagazin
    913.1h  1.34% Programmende
    892.8h  1.31% Talkshow
    891.7h  1.30% Religionsmagazin
    733.8h  1.07% Magazin
    708.9h  1.04% E-Sport
    647.7h  0.95% Sitcom
    602.2h  0.88% Wetterbericht
    601.0h  0.88% Börsenmagazin
    561.5h  0.82% Wirtschaftsmagazin
    532.0h  0.78% Wissensmagazin
    512.5h  0.75% Quiz
    502.1h  0.73% Musikmagazin
    495.7h  0.73% Dramaserie
    490.3h  0.72% Gesundheitsmagazin
    469.9h  0.69% Telenovela
    447.6h  0.65% Gerichtsshow
