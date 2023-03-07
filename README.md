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

**96** channels, **91,989.4** hours playtime between **2023-01-17** and **2023-03-08**


### playtime per genre (top 30)

    6492.9h 7.06% Nachrichten
    4614.3h 5.02% Verkaufsshow
    3873.3h 4.21% Krimiserie
    3124.0h 3.40% Werbesendung
    3010.7h 3.27% Dokusoap
    2753.9h 2.99% Dokureihe
    2688.7h 2.92% Regionalmagazin
    2267.5h 2.46% Dokumentation
    2221.6h 2.42% *unknown*
    1757.9h 1.91% Animationsserie
    1683.8h 1.83% Infomercial
    1666.1h 1.81% Zeichentrickserie
    1487.3h 1.62% Comedyserie
    1300.8h 1.41% Morgenmagazin
    1241.6h 1.35% Programmende
    1211.5h 1.32% Religionsmagazin
    1207.8h 1.31% Talkshow
    959.3h  1.04% E-Sport
    958.1h  1.04% Magazin
    868.2h  0.94% Sitcom
    845.9h  0.92% Börsenmagazin
    809.6h  0.88% Wetterbericht
    745.8h  0.81% Wirtschaftsmagazin
    722.1h  0.78% Wissensmagazin
    687.5h  0.75% Quiz
    676.7h  0.74% Musikmagazin
    662.8h  0.72% Dramaserie
    645.5h  0.70% Gesundheitsmagazin
    633.1h  0.69% Telenovela
    597.2h  0.65% Sportmagazin
