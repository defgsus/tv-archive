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

**96** channels, **41,006.5** hours playtime between **2023-01-17** and **2023-02-08**


### playtime per genre (top 30)

    2857.8h 6.97% Nachrichten
    2135.8h 5.21% Verkaufsshow
    1737.7h 4.24% Krimiserie
    1425.7h 3.48% Dokusoap
    1396.3h 3.41% Werbesendung
    1254.8h 3.06% Dokureihe
    1182.6h 2.88% Regionalmagazin
    1019.2h 2.49% Dokumentation
    1018.5h 2.48% *unknown*
    794.6h  1.94% Zeichentrickserie
    767.7h  1.87% Infomercial
    733.3h  1.79% Animationsserie
    690.2h  1.68% Comedyserie
    571.9h  1.39% Morgenmagazin
    549.4h  1.34% Religionsmagazin
    526.3h  1.28% Talkshow
    516.2h  1.26% Programmende
    468.6h  1.14% Magazin
    434.3h  1.06% E-Sport
    375.2h  0.91% Sitcom
    359.1h  0.88% Börsenmagazin
    351.6h  0.86% Wetterbericht
    342.4h  0.84% Wirtschaftsmagazin
    329.2h  0.80% Wissensmagazin
    320.6h  0.78% Quiz
    309.1h  0.75% Dramaserie
    307.2h  0.75% Musikmagazin
    289.7h  0.71% Gesundheitsmagazin
    284.2h  0.69% Telenovela
    272.2h  0.66% Sportmagazin
