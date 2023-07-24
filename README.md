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

**96** channels, **341,067.3** hours playtime between **2023-01-17** and **2023-07-25**


### playtime per genre (top 30)

    22646.7h 6.64% Nachrichten
    16281.0h 4.77% Verkaufsshow
    13705.7h 4.02% Krimiserie
    11462.2h 3.36% Werbesendung
    11140.3h 3.27% Dokureihe
    10302.0h 3.02% Dokusoap
    9763.6h  2.86% Regionalmagazin
    8575.0h  2.51% Dokumentation
    8313.0h  2.44% *unknown*
    6473.3h  1.90% Zeichentrickserie
    6233.8h  1.83% Infomercial
    6012.5h  1.76% Animationsserie
    5623.0h  1.65% Comedyserie
    4764.5h  1.40% Morgenmagazin
    4528.4h  1.33% Religionsmagazin
    4512.5h  1.32% Talkshow
    4070.5h  1.19% Magazin
    3941.2h  1.16% Programmende
    3367.8h  0.99% E-Sport
    3224.4h  0.95% Sitcom
    3192.9h  0.94% Wetterbericht
    3079.3h  0.90% Börsenmagazin
    2728.1h  0.80% Quiz
    2667.3h  0.78% Musikmagazin
    2630.5h  0.77% Wirtschaftsmagazin
    2614.6h  0.77% Komödie
    2595.4h  0.76% Wissensmagazin
    2347.1h  0.69% Telenovela
    2252.4h  0.66% Sportmagazin
    2199.6h  0.64% Reportagereihe
