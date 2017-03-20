library("wordcloud")
library("RColorBrewer")

foorumiSagedused <- read.csv(file="lemmadeSagedusloend.csv", sep=";")
head(foorumiSagedused)

varvid <- brewer.pal(8,"Dark2")

tiff("foorumiSonapilv.tiff", width=18.5, height=10.5, units="cm", compression = "lzw", res = 300)
wordcloud(words = foorumiSagedused$Lemma, freq = foorumiSagedused$Sagedus, scale=c(3,.2), min.freq = 2, colors=varvid, rot.per=.15, random.order=F)
dev.off()
