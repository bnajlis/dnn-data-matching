require(csv)
df = read.csv("febrl-data/dedu-dsgen/dataset_A_10000.csv")

hist(dataset_A_1000$state, 
     main="",
     xlab="Age",
     ylab = "Number of patients",
     col="blue",
     breaks=20)
