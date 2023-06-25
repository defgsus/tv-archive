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

**96** channels, **289,114.0** hours playtime between **2023-01-17** and **2023-06-26**


### playtime per genre (top 30)

    19251.9h 6.66% Nachrichten
    13901.1h 4.81% Verkaufsshow
    11554.1h 4.00% Krimiserie
    9654.3h  3.34% Werbesendung
    9405.5h  3.25% Dokureihe
    8724.5h  3.02% Dokusoap
    8246.0h  2.85% Regionalmagazin
    7377.9h  2.55% Dokumentation
    7196.7h  2.49% *unknown*
    5513.9h  1.91% Zeichentrickserie
    5295.2h  1.83% Infomercial
    5102.5h  1.76% Animationsserie
    4785.0h  1.66% Comedyserie
    4011.7h  1.39% Morgenmagazin
    3831.1h  1.33% Talkshow
    3815.2h  1.32% Religionsmagazin
    3540.6h  1.22% Programmende
    3388.9h  1.17% Magazin
    2861.9h  0.99% E-Sport
    2736.3h  0.95% Sitcom
    2659.1h  0.92% Wetterbericht
    2550.7h  0.88% Börsenmagazin
    2262.6h  0.78% Musikmagazin
    2258.1h  0.78% Quiz
    2257.7h  0.78% Wirtschaftsmagazin
    2220.3h  0.77% Wissensmagazin
    2196.1h  0.76% Komödie
    2036.0h  0.70% Telenovela
    1950.4h  0.67% Sportmagazin
    1909.1h  0.66% Wirtschaftstalk
