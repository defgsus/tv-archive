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

**96** channels, **95,680.8** hours playtime between **2023-01-17** and **2023-03-10**


### playtime per genre (top 30)

    6771.2h 7.08% Nachrichten
    4803.5h 5.02% Verkaufsshow
    4035.9h 4.22% Krimiserie
    3246.6h 3.39% Werbesendung
    3130.6h 3.27% Dokusoap
    2862.6h 2.99% Dokureihe
    2840.2h 2.97% Regionalmagazin
    2345.1h 2.45% Dokumentation
    2306.0h 2.41% *unknown*
    1832.5h 1.92% Animationsserie
    1752.3h 1.83% Infomercial
    1724.9h 1.80% Zeichentrickserie
    1560.3h 1.63% Comedyserie
    1370.2h 1.43% Morgenmagazin
    1311.6h 1.37% Programmende
    1261.2h 1.32% Talkshow
    1253.1h 1.31% Religionsmagazin
    1001.8h 1.05% Magazin
    993.4h  1.04% E-Sport
    916.0h  0.96% Sitcom
    875.4h  0.91% Börsenmagazin
    844.5h  0.88% Wetterbericht
    783.4h  0.82% Wirtschaftsmagazin
    750.4h  0.78% Wissensmagazin
    718.5h  0.75% Quiz
    702.9h  0.73% Musikmagazin
    695.0h  0.73% Dramaserie
    675.0h  0.71% Telenovela
    672.5h  0.70% Gesundheitsmagazin
    619.3h  0.65% Gerichtsshow
