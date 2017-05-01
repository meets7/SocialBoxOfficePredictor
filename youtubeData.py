import sys
import pandas as pd
import utility as uti
import youtubeAPI as api
import csv

if __name__ == "__main__":
    csvFile = sys.argv[1]		# gets called in
    outputFile = sys.argv[2]
    startrow = int(sys.argv[3])
    endrow = int(sys.argv[4])

    data = pd.read_csv(csvFile, dtype='object')
    writeCSV = csv.writer(open(outputFile, "ab")) # change to wb to overwrite, ab to append

    for i in range(startrow, endrow): # 0 to 7, 7 to 10 and so on ..
        if i == 0:      # add this row only if we starting from first row of data frame
            writeCSV.writerow(["movie_title", "year", "view_count", "like_count", "dislike_count"])
        movieTitleDF = data['movie_title'].iloc[i]
        movieYearDF = data['title_year'].iloc[i]
        movieTitle = uti.plaintext(movieTitleDF)
        if not movieYearDF == "":
            searchText = movieTitle + " " + "trailer official"
        else:
            searchText = movieTitle + " " + movieYearDF + " " + "trailer official"
        stats = api.youtubeSearch(searchText) # get viewcount, likecount, dislike count dictionary
        writeCSV.writerow([movieTitle, movieYearDF, stats['viewCount'], stats['likeCount'], stats['dislikeCount']])
