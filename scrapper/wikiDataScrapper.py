import wptools
import re
import wikipedia

wikisearchresults = wikipedia.search("Dhoom 3 film",10,False)
wikipage = wikipedia.WikipediaPage(wikisearchresults[0])
boxOfficeSection =  wikipage.section('Box office')
pattern = r"(?<=US\$)([0-9]+)"
boxOfficeNumbers = [float(n) for n in re.findall(pattern,boxOfficeSection)]
print max(boxOfficeNumbers)

# fela = wptools.page('Dhoom 3', verbose='false').get_parse()
# # print fela.infobox['gross']

# if fela.infobox['gross'] == "{{Estimation}}":

	