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

**96** channels, **86,593.1** hours playtime between **2023-01-17** and **2023-03-05**


### playtime per genre (top 30)

    6115.9h 7.06% Nachrichten
    4361.8h 5.04% Verkaufsshow
    3664.3h 4.23% Krimiserie
    2945.6h 3.40% Werbesendung
    2839.0h 3.28% Dokusoap
    2602.2h 3.01% Dokureihe
    2557.3h 2.95% Regionalmagazin
    2087.1h 2.41% Dokumentation
    2028.4h 2.34% *unknown*
    1650.5h 1.91% Animationsserie
    1586.2h 1.83% Infomercial
    1581.5h 1.83% Zeichentrickserie
    1399.1h 1.62% Comedyserie
    1238.0h 1.43% Morgenmagazin
    1177.4h 1.36% Programmende
    1131.6h 1.31% Talkshow
    1128.8h 1.30% Religionsmagazin
    917.1h  1.06% Magazin
    899.8h  1.04% E-Sport
    823.5h  0.95% Sitcom
    775.3h  0.90% Börsenmagazin
    763.0h  0.88% Wetterbericht
    700.5h  0.81% Wirtschaftsmagazin
    676.4h  0.78% Wissensmagazin
    644.0h  0.74% Quiz
    631.1h  0.73% Musikmagazin
    627.5h  0.72% Dramaserie
    618.7h  0.71% Gesundheitsmagazin
    593.2h  0.69% Telenovela
    559.7h  0.65% Gerichtsshow
