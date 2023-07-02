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

**96** channels, **301,652.5** hours playtime between **2023-01-17** and **2023-07-03**


### playtime per genre (top 30)

    20093.3h 6.66% Nachrichten
    14480.8h 4.80% Verkaufsshow
    12068.9h 4.00% Krimiserie
    10085.5h 3.34% Werbesendung
    9805.8h  3.25% Dokureihe
    9138.7h  3.03% Dokusoap
    8613.5h  2.86% Regionalmagazin
    7640.1h  2.53% Dokumentation
    7474.9h  2.48% *unknown*
    5750.9h  1.91% Zeichentrickserie
    5521.5h  1.83% Infomercial
    5315.7h  1.76% Animationsserie
    5001.8h  1.66% Comedyserie
    4199.2h  1.39% Morgenmagazin
    4015.8h  1.33% Talkshow
    3986.7h  1.32% Religionsmagazin
    3639.2h  1.21% Programmende
    3549.3h  1.18% Magazin
    2989.4h  0.99% E-Sport
    2853.1h  0.95% Sitcom
    2786.0h  0.92% Wetterbericht
    2661.4h  0.88% Börsenmagazin
    2369.0h  0.79% Quiz
    2366.5h  0.78% Musikmagazin
    2348.0h  0.78% Wirtschaftsmagazin
    2316.5h  0.77% Wissensmagazin
    2302.6h  0.76% Komödie
    2126.5h  0.70% Telenovela
    2022.1h  0.67% Sportmagazin
    1965.0h  0.65% Wirtschaftstalk
