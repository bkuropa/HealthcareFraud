library(dplyr)
my.path <- getwd()

pt.D <- read.csv(paste(my.path,"/","PartD_Prescriber_PUF_NPI_Drug_13-002.txt",sep=""),sep="\t",header=TRUE)
op.rsrch <- read.csv(paste(my.path,"/","OP_DTL_RSRCH_PGYR2017_P06292018.csv",sep=""),sep=",",header=TRUE)
op.gnrl <- read.csv(paste(my.path,"/","OP_DTL_GNRL_PGYR2017_P06292018.csv",sep=""),sep=",",header=TRUE)

mkStat <- read.csv(paste(my.path,"/","MarketingStatus.txt",sep=""),sep="\t",header=TRUE)

mkStatID <- as.data.frame(c(("Prescription"),("Over-the-counter"),("Discontinued"),("Other")))
mkStatID <- cbind(c(1,2,3,4),mkStatID)
colnames(mkStatID) <- c("MarketingStatusID","Status")

op.rsrch <- read.csv(paste(my.path,"/","OP_DTL_RSRCH_PGYR2017_P06292018.csv",sep=""),sep=",",header=TRUE)
op.gnrl <- read.csv(paste(my.path,"/","OP_DTL_GNRL_PGYR2017_P06292018.csv",sep=""),sep=",",header=TRUE)

#Read and use FDA products for statistics 
mkStat2 <- merge(mkStat,mkStatID,on="MarketingStatusID")
fda.prod <- read.csv(paste(my.path,"/","Products.txt",sep=""),sep="\t",header=TRUE)

leie <- read.csv(paste(my.path,"/","LEIE_UPDATED.csv",sep=""),sep=",",header=TRUE)

drug.key <- paste(mkStat2$ApplNo,mkStat2$ProductNo,sep="-") 
mkStat2 <- cbind(mkStat2,drug.key)

#Join Drug info with drug status column (i.e. "Discontinued", "Active", etc.)
drug.key <- paste(fda.prod$ApplNo,fda.prod$ProductNo,sep="-")
fda.prod <- cbind(fda.prod,drug.key)
fda.drugs <- merge(fda.prod,mkStat2,on="drug.key")
write.csv(fda.drugs,file="FDA-drugs.csv")

#Quick stats of both files to be cleaned in Excel
dim(spr.frm)
summary(spr.frm)
View(summary(spr.frm))
View(summary(spr.frm[,40:47]))
write.csv(summary(spr.frm[,c(40,42,44,46)]),"stats2.csv")
dim(clpsd)
write.csv(summary(clpsd[,27:30]),"stats3.csv")

install.packages("benford.analysis")
library(benford.analysis)




#Import both finalized datasets
spr.frm <- read.csv(paste(my.path,"/","superframe.csv",sep=""),sep=",",header=TRUE)
clpsd <- read.csv(paste(my.path,"/","DataCollaspedbyGenericPerDoctor.csv",sep=""),sep=",",header=TRUE)

#Benford object -> Benford dataframe => Benford plot
spr.bfd <- benford(spr.frm[,46])
bfd.df <- spr.bfd$bfd
plot(bfd.spr)

#Benford Law graphic
ggplot() +
geom_col(data = bfd.df, aes(x = digits, y = data.dist,colour='Digits')) +
geom_line(data = bad.df, aes(x = digits, y = benford.dist,colour = 'Calc\'d')) +
  ggtitle('Benford\'s Law Analysis') +
xlab('Total_Drug_Cost\'s First Two Digits') +
ylab('Frequency') + 
  scale_x_continuous(breaks=seq(0,99,5)) +
  scale_color_manual(values = c('Digits' = 'grey','Calc\'d' = 'red')) +
 labs(color = 'Benford\'s Law') +
  theme(legend.position = c(0.60,.50))
plot(bfd.spr)

ggplot() +
  geom_boxplot(data=clpsd,aes(x=))
