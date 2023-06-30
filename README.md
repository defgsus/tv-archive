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

**96** channels, **298,047.5** hours playtime between **2023-01-17** and **2023-07-01**


### playtime per genre (top 30)

    19929.3h 6.69% Nachrichten
    14332.8h 4.81% Verkaufsshow
    11925.4h 4.00% Krimiserie
    9947.2h  3.34% Werbesendung
    9667.4h  3.24% Dokureihe
    9049.2h  3.04% Dokusoap
    8562.5h  2.87% Regionalmagazin
    7555.2h  2.53% Dokumentation
    7385.4h  2.48% *unknown*
    5684.6h  1.91% Zeichentrickserie
    5455.8h  1.83% Infomercial
    5248.2h  1.76% Animationsserie
    4967.9h  1.67% Comedyserie
    4185.4h  1.40% Morgenmagazin
    3964.9h  1.33% Talkshow
    3918.1h  1.31% Religionsmagazin
    3610.5h  1.21% Programmende
    3503.6h  1.18% Magazin
    2944.1h  0.99% E-Sport
    2827.7h  0.95% Sitcom
    2749.4h  0.92% Wetterbericht
    2656.4h  0.89% Börsenmagazin
    2356.0h  0.79% Quiz
    2335.4h  0.78% Wirtschaftsmagazin
    2333.4h  0.78% Musikmagazin
    2293.9h  0.77% Wissensmagazin
    2225.5h  0.75% Komödie
    2123.7h  0.71% Telenovela
    1996.7h  0.67% Sportmagazin
    1953.0h  0.66% Wirtschaftstalk
