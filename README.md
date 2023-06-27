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

**96** channels, **292,671.4** hours playtime between **2023-01-17** and **2023-06-28**


### playtime per genre (top 30)

    19522.2h 6.67% Nachrichten
    14074.3h 4.81% Verkaufsshow
    11705.1h 4.00% Krimiserie
    9773.2h  3.34% Werbesendung
    9517.8h  3.25% Dokureihe
    8851.3h  3.02% Dokusoap
    8370.7h  2.86% Regionalmagazin
    7453.2h  2.55% Dokumentation
    7277.2h  2.49% *unknown*
    5584.5h  1.91% Zeichentrickserie
    5358.1h  1.83% Infomercial
    5161.9h  1.76% Animationsserie
    4856.6h  1.66% Comedyserie
    4081.2h  1.39% Morgenmagazin
    3875.1h  1.32% Talkshow
    3855.5h  1.32% Religionsmagazin
    3568.7h  1.22% Programmende
    3422.9h  1.17% Magazin
    2905.8h  0.99% E-Sport
    2771.3h  0.95% Sitcom
    2696.6h  0.92% Wetterbericht
    2604.3h  0.89% Börsenmagazin
    2302.2h  0.79% Quiz
    2290.0h  0.78% Musikmagazin
    2287.4h  0.78% Wirtschaftsmagazin
    2248.4h  0.77% Wissensmagazin
    2205.4h  0.75% Komödie
    2071.0h  0.71% Telenovela
    1974.7h  0.67% Sportmagazin
    1915.7h  0.65% Wirtschaftstalk
