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

**96** channels, **342,862.0** hours playtime between **2023-01-17** and **2023-07-26**


### playtime per genre (top 30)

    22777.5h 6.64% Nachrichten
    16356.2h 4.77% Verkaufsshow
    13808.4h 4.03% Krimiserie
    11522.8h 3.36% Werbesendung
    11194.2h 3.26% Dokureihe
    10349.0h 3.02% Dokusoap
    9826.8h  2.87% Regionalmagazin
    8631.3h  2.52% Dokumentation
    8351.9h  2.44% *unknown*
    6505.2h  1.90% Zeichentrickserie
    6266.6h  1.83% Infomercial
    6048.1h  1.76% Animationsserie
    5657.2h  1.65% Comedyserie
    4796.4h  1.40% Morgenmagazin
    4550.6h  1.33% Religionsmagazin
    4531.4h  1.32% Talkshow
    4096.9h  1.19% Magazin
    3955.1h  1.15% Programmende
    3387.7h  0.99% E-Sport
    3240.1h  0.95% Sitcom
    3211.1h  0.94% Wetterbericht
    3106.1h  0.91% Börsenmagazin
    2737.1h  0.80% Quiz
    2684.6h  0.78% Musikmagazin
    2644.1h  0.77% Wirtschaftsmagazin
    2626.3h  0.77% Komödie
    2603.2h  0.76% Wissensmagazin
    2361.3h  0.69% Telenovela
    2263.6h  0.66% Sportmagazin
    2198.2h  0.64% Reportagereihe
