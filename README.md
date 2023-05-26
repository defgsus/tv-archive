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

**96** channels, **235,358.6** hours playtime between **2023-01-17** and **2023-05-27**


### playtime per genre (top 30)

    15808.1h 6.72% Nachrichten
    11392.3h 4.84% Verkaufsshow
    9523.5h  4.05% Krimiserie
    7816.3h  3.32% Werbesendung
    7650.1h  3.25% Dokureihe
    7011.8h  2.98% Dokusoap
    6786.6h  2.88% Regionalmagazin
    5979.4h  2.54% Dokumentation
    5832.1h  2.48% *unknown*
    4402.8h  1.87% Zeichentrickserie
    4315.6h  1.83% Infomercial
    4223.8h  1.79% Animationsserie
    3940.9h  1.67% Comedyserie
    3285.1h  1.40% Morgenmagazin
    3127.2h  1.33% Programmende
    3106.9h  1.32% Talkshow
    3074.4h  1.31% Religionsmagazin
    2717.7h  1.15% Magazin
    2355.9h  1.00% E-Sport
    2225.6h  0.95% Sitcom
    2166.3h  0.92% Börsenmagazin
    2141.4h  0.91% Wetterbericht
    1860.2h  0.79% Wirtschaftsmagazin
    1829.0h  0.78% Wissensmagazin
    1824.5h  0.78% Musikmagazin
    1824.1h  0.78% Quiz
    1678.1h  0.71% Telenovela
    1633.8h  0.69% Komödie
    1631.6h  0.69% Sportmagazin
    1574.3h  0.67% Gesundheitsmagazin
