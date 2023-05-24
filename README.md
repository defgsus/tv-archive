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

**96** channels, **231,774.7** hours playtime between **2023-01-17** and **2023-05-25**


### playtime per genre (top 30)

    15567.0h 6.72% Nachrichten
    11211.3h 4.84% Verkaufsshow
    9368.3h  4.04% Krimiserie
    7706.2h  3.32% Werbesendung
    7542.6h  3.25% Dokureihe
    6894.8h  2.97% Dokusoap
    6665.6h  2.88% Regionalmagazin
    5907.8h  2.55% Dokumentation
    5731.5h  2.47% *unknown*
    4322.8h  1.87% Zeichentrickserie
    4248.0h  1.83% Infomercial
    4174.6h  1.80% Animationsserie
    3877.7h  1.67% Comedyserie
    3216.6h  1.39% Morgenmagazin
    3099.6h  1.34% Programmende
    3054.0h  1.32% Talkshow
    3034.3h  1.31% Religionsmagazin
    2664.2h  1.15% Magazin
    2323.3h  1.00% E-Sport
    2191.6h  0.95% Sitcom
    2129.5h  0.92% Börsenmagazin
    2105.5h  0.91% Wetterbericht
    1826.0h  0.79% Wirtschaftsmagazin
    1802.5h  0.78% Wissensmagazin
    1794.3h  0.77% Musikmagazin
    1790.3h  0.77% Quiz
    1639.9h  0.71% Telenovela
    1625.3h  0.70% Komödie
    1616.8h  0.70% Sportmagazin
    1561.9h  0.67% Gesundheitsmagazin
