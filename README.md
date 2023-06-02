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

**96** channels, **247,924.0** hours playtime between **2023-01-17** and **2023-06-03**


### playtime per genre (top 30)

    16587.2h 6.69% Nachrichten
    11980.8h 4.83% Verkaufsshow
    9965.5h  4.02% Krimiserie
    8230.6h  3.32% Werbesendung
    8049.4h  3.25% Dokureihe
    7415.8h  2.99% Dokusoap
    7117.1h  2.87% Regionalmagazin
    6354.0h  2.56% Dokumentation
    6156.6h  2.48% *unknown*
    4657.1h  1.88% Zeichentrickserie
    4539.9h  1.83% Infomercial
    4428.3h  1.79% Animationsserie
    4133.5h  1.67% Comedyserie
    3443.8h  1.39% Morgenmagazin
    3270.3h  1.32% Talkshow
    3241.2h  1.31% Religionsmagazin
    3224.4h  1.30% Programmende
    2862.3h  1.15% Magazin
    2478.4h  1.00% E-Sport
    2327.7h  0.94% Sitcom
    2260.7h  0.91% Wetterbericht
    2255.9h  0.91% Börsenmagazin
    1953.6h  0.79% Wirtschaftsmagazin
    1926.1h  0.78% Quiz
    1923.8h  0.78% Wissensmagazin
    1922.4h  0.78% Musikmagazin
    1795.5h  0.72% Komödie
    1760.6h  0.71% Telenovela
    1707.1h  0.69% Sportmagazin
    1634.0h  0.66% Gesundheitsmagazin
