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

**97** channels, **588,374.8** hours playtime between **2023-01-17** and **2023-12-11**


### playtime per genre (top 30)

    38627.4h 6.57% Nachrichten
    28219.7h 4.80% Verkaufsshow
    23763.8h 4.04% Krimiserie
    19998.1h 3.40% Werbesendung
    19142.6h 3.25% Dokureihe
    17716.6h 3.01% Dokusoap
    16992.2h 2.89% Regionalmagazin
    15048.7h 2.56% Dokumentation
    14403.3h 2.45% *unknown*
    10872.6h 1.85% Zeichentrickserie
    10722.8h 1.82% Infomercial
    10445.2h 1.78% Animationsserie
    9066.8h  1.54% Comedyserie
    8368.7h  1.42% Morgenmagazin
    7975.2h  1.36% Religionsmagazin
    7892.4h  1.34% Talkshow
    7575.8h  1.29% Magazin
    5839.5h  0.99% Programmende
    5771.2h  0.98% E-Sport
    5681.0h  0.97% Sitcom
    5386.5h  0.92% Wetterbericht
    5337.1h  0.91% Börsenmagazin
    4876.9h  0.83% Quiz
    4592.1h  0.78% Komödie
    4483.9h  0.76% Wissensmagazin
    4396.9h  0.75% Wirtschaftsmagazin
    4276.1h  0.73% Musikmagazin
    4258.1h  0.72% Telenovela
    4208.1h  0.72% Realityshow
    4166.2h  0.71% Politikmagazin
