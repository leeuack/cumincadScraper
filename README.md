# cumincadScraper
This repo includes a site-specific ([CumInCAD](http://papers.cumincad.org/)) Python crawler.

[CumInCAD](http://papers.cumincad.org/) is a digital archiving platform supported by several conferences and journals in computer-aided architectural design research society.
Users can scrape all papers in CumInCAD which includes at least one word of keywords (search_words).

the main() function has one argument, total number of papers.
The default value of the argument is 15260, since currently (2020.10.12) the maximum numbers of paper is 15176.

To run the file, users can write those codes

```
$python main()
```

or
with the total number of publications arugment

```
$python main(300)
```

