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

**96** channels, **35,581.2** hours playtime between **2023-01-17** and **2023-02-05**


### playtime per genre (top 30)

    2485.6h 6.99% Nachrichten
    1875.6h 5.27% Verkaufsshow
    1496.3h 4.21% Krimiserie
    1243.1h 3.49% Dokusoap
    1198.8h 3.37% Werbesendung
    1074.2h 3.02% Dokureihe
    1034.3h 2.91% Regionalmagazin
    884.6h  2.49% Dokumentation
    877.8h  2.47% *unknown*
    693.5h  1.95% Zeichentrickserie
    673.8h  1.89% Infomercial
    630.8h  1.77% Animationsserie
    602.2h  1.69% Comedyserie
    495.0h  1.39% Morgenmagazin
    460.6h  1.29% Religionsmagazin
    453.5h  1.27% Talkshow
    453.5h  1.27% Programmende
    407.7h  1.15% Magazin
    385.6h  1.08% E-Sport
    329.2h  0.93% Sitcom
    306.1h  0.86% Börsenmagazin
    304.0h  0.85% Wetterbericht
    296.5h  0.83% Wirtschaftsmagazin
    285.2h  0.80% Wissensmagazin
    281.4h  0.79% Dramaserie
    276.4h  0.78% Quiz
    265.6h  0.75% Musikmagazin
    255.8h  0.72% Gesundheitsmagazin
    252.2h  0.71% Telenovela
    237.7h  0.67% Realityshow
