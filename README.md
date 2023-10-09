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

**97** channels, **478,903.6** hours playtime between **2023-01-17** and **2023-10-10**


### playtime per genre (top 30)

    31534.4h 6.58% Nachrichten
    22828.3h 4.77% Verkaufsshow
    19270.2h 4.02% Krimiserie
    16173.1h 3.38% Werbesendung
    15799.0h 3.30% Dokureihe
    14647.7h 3.06% Dokusoap
    13769.5h 2.88% Regionalmagazin
    12100.7h 2.53% Dokumentation
    11443.9h 2.39% *unknown*
    8992.5h  1.88% Zeichentrickserie
    8723.2h  1.82% Infomercial
    8517.2h  1.78% Animationsserie
    7669.1h  1.60% Comedyserie
    6752.3h  1.41% Morgenmagazin
    6430.1h  1.34% Religionsmagazin
    6360.4h  1.33% Talkshow
    5960.1h  1.24% Magazin
    5001.3h  1.04% Programmende
    4732.8h  0.99% E-Sport
    4545.2h  0.95% Sitcom
    4472.7h  0.93% Wetterbericht
    4325.3h  0.90% Börsenmagazin
    4017.6h  0.84% Quiz
    3729.7h  0.78% Komödie
    3659.8h  0.76% Musikmagazin
    3606.7h  0.75% Wirtschaftsmagazin
    3601.9h  0.75% Wissensmagazin
    3398.2h  0.71% Telenovela
    3234.7h  0.68% Politikmagazin
    3114.4h  0.65% Reportagereihe
