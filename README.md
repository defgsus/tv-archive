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

**96** channels, **93,859.4** hours playtime between **2023-01-17** and **2023-03-09**


### playtime per genre (top 30)

    6638.7h 7.07% Nachrichten
    4705.1h 5.01% Verkaufsshow
    3957.7h 4.22% Krimiserie
    3184.9h 3.39% Werbesendung
    3062.6h 3.26% Dokusoap
    2821.3h 3.01% Dokureihe
    2772.4h 2.95% Regionalmagazin
    2307.5h 2.46% Dokumentation
    2262.0h 2.41% *unknown*
    1794.2h 1.91% Animationsserie
    1717.3h 1.83% Infomercial
    1697.5h 1.81% Zeichentrickserie
    1533.5h 1.63% Comedyserie
    1335.5h 1.42% Morgenmagazin
    1276.5h 1.36% Programmende
    1237.0h 1.32% Talkshow
    1227.4h 1.31% Religionsmagazin
    977.8h  1.04% Magazin
    969.9h  1.03% E-Sport
    896.8h  0.96% Sitcom
    860.0h  0.92% Börsenmagazin
    826.7h  0.88% Wetterbericht
    764.3h  0.81% Wirtschaftsmagazin
    741.2h  0.79% Wissensmagazin
    704.5h  0.75% Quiz
    688.3h  0.73% Musikmagazin
    676.4h  0.72% Dramaserie
    664.4h  0.71% Gesundheitsmagazin
    654.2h  0.70% Telenovela
    609.5h  0.65% Gerichtsshow
