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

**96** channels, **73,840.5** hours playtime between **2023-01-17** and **2023-02-26**


### playtime per genre (top 30)

    5222.4h 7.07% Nachrichten
    3759.2h 5.09% Verkaufsshow
    3127.9h 4.24% Krimiserie
    2509.6h 3.40% Werbesendung
    2459.0h 3.33% Dokusoap
    2201.5h 2.98% Dokureihe
    2165.7h 2.93% Regionalmagazin
    1782.9h 2.41% Dokumentation
    1779.5h 2.41% *unknown*
    1391.5h 1.88% Animationsserie
    1366.3h 1.85% Zeichentrickserie
    1354.5h 1.83% Infomercial
    1199.2h 1.62% Comedyserie
    1052.1h 1.42% Morgenmagazin
    990.1h  1.34% Programmende
    961.7h  1.30% Religionsmagazin
    961.1h  1.30% Talkshow
    793.0h  1.07% Magazin
    764.5h  1.04% E-Sport
    698.5h  0.95% Sitcom
    651.2h  0.88% Wetterbericht
    646.4h  0.88% Börsenmagazin
    599.7h  0.81% Wirtschaftsmagazin
    578.4h  0.78% Wissensmagazin
    551.4h  0.75% Quiz
    541.5h  0.73% Musikmagazin
    538.0h  0.73% Dramaserie
    525.2h  0.71% Gesundheitsmagazin
    507.2h  0.69% Telenovela
    481.2h  0.65% Gerichtsshow
