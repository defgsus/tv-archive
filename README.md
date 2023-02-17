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

**96** channels, **59,240.7** hours playtime between **2023-01-17** and **2023-02-18**


### playtime per genre (top 30)

    4183.6h 7.06% Nachrichten
    3040.2h 5.13% Verkaufsshow
    2532.2h 4.27% Krimiserie
    2034.0h 3.43% Dokusoap
    2001.9h 3.38% Werbesendung
    1737.5h 2.93% Regionalmagazin
    1721.5h 2.91% Dokureihe
    1469.5h 2.48% Dokumentation
    1467.0h 2.48% *unknown*
    1120.7h 1.89% Zeichentrickserie
    1091.1h 1.84% Infomercial
    1090.4h 1.84% Animationsserie
    988.4h  1.67% Comedyserie
    859.2h  1.45% Morgenmagazin
    781.5h  1.32% Programmende
    777.6h  1.31% Talkshow
    767.3h  1.30% Religionsmagazin
    657.5h  1.11% Magazin
    622.7h  1.05% E-Sport
    559.2h  0.94% Sitcom
    530.0h  0.89% Börsenmagazin
    518.8h  0.88% Wetterbericht
    497.7h  0.84% Wirtschaftsmagazin
    462.5h  0.78% Wissensmagazin
    456.2h  0.77% Quiz
    441.3h  0.74% Dramaserie
    435.2h  0.73% Musikmagazin
    420.9h  0.71% Gesundheitsmagazin
    420.7h  0.71% Telenovela
    387.9h  0.65% Gerichtsshow
