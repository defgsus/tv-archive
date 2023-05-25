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

**96** channels, **233,563.2** hours playtime between **2023-01-17** and **2023-05-26**


### playtime per genre (top 30)

    15687.5h 6.72% Nachrichten
    11301.2h 4.84% Verkaufsshow
    9455.5h  4.05% Krimiserie
    7761.6h  3.32% Werbesendung
    7601.8h  3.25% Dokureihe
    6952.2h  2.98% Dokusoap
    6727.9h  2.88% Regionalmagazin
    5953.1h  2.55% Dokumentation
    5774.3h  2.47% *unknown*
    4360.5h  1.87% Zeichentrickserie
    4282.4h  1.83% Infomercial
    4201.0h  1.80% Animationsserie
    3915.7h  1.68% Comedyserie
    3250.8h  1.39% Morgenmagazin
    3113.5h  1.33% Programmende
    3072.4h  1.32% Talkshow
    3055.6h  1.31% Religionsmagazin
    2694.3h  1.15% Magazin
    2333.5h  1.00% E-Sport
    2207.6h  0.95% Sitcom
    2140.6h  0.92% Börsenmagazin
    2123.2h  0.91% Wetterbericht
    1843.3h  0.79% Wirtschaftsmagazin
    1817.9h  0.78% Wissensmagazin
    1811.2h  0.78% Musikmagazin
    1805.9h  0.77% Quiz
    1658.5h  0.71% Telenovela
    1626.1h  0.70% Komödie
    1624.0h  0.70% Sportmagazin
    1567.3h  0.67% Gesundheitsmagazin
