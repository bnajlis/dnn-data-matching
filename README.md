# Applications of Deep Learning and Parallel Processing Frameworks in Data Matching

## What is Data Matching, Record Linkage, Entity Resolution?

* “Is the task of identifying, matching and merging records that correspond to the same entities from several databases:
    * Biomedical records (patients),
    * People (customers, tax payers, travellers),
    * Publications or citations,
    * Consumer products,
    * Businesses”

* Traditional application of machine/statistical learning and NLP
* Major Challenges are:
    * Different data set schemas, different levels of field granularity 
    * Computation Complexity on Big Data sets: O(n2) problem
    * Lack of unique entity identifiers and data quality
    * Lack of training data containing the True Matching status

## Research Project Objective

* Subject of research project is to improve Data Matching using parallel programming and Deep Neural Networks
* Parallel programming frameworks like Spark, Apache Beam, can dramatically increase the performance of computing pair comparisons to find matches, due to O(n2) complexity of the problem
* Deep Neural Networks have shown to improve accuracy on traditional machine learning applications
* Open datasets available through FEBRL project (Freely Extensible biomedical record linkage) from Department of Computer Science, Australian National University, Canberra

## Why is this interesting and exciting?
* A majority of Data Science research work assumes a clean, deduplicated dataset as a pre-condition. 80% of data science field work is deduplication, cleanup and wrangling
* Not enough research papers focused on data quality as an issue for Data Science
* A general problem and solution, applicable to multiple data domains
* A novel chance to apply Deep Neural Networks in this research field
* As data set sizes keep increasing, the application of parallel programming frameworks in this field becomes a necessity

## Summary of Traditional Data Matching Process

![Source: “Data Matching – Concepts and Techniques for Record Linkage, Entity Resolution and Duplicate Detection” – Peter Christen (Research School of Computer Science, The Australian National University, Canberra, Australia) – Springer, 2012
Alt](traditional-data-matching-process.png)

### 1- Pre-processing
Remove stop words, tokenization, tagging, expand abbreviations, correct misspellings. Segment attributes into smaller, consistent attributes (name, address, phone, email). Attribute validation and correction.
### 2- Indexing (Generating candidate record pairs)
Blocking criteria
Soundex, Phonex, Phonix, NYIIS, ONCA, Double Methaphone, Fuzzy Soundex, Sorted Neighbourhood, Q-Gram based indexing, Suffix-array based index, Canopy Clustering, Mapping Based index
### 3- Record Pair Comparison (Computing similarity score)
Text attributes: Edit distance comparison (Levenshtein, Damerau, Smith-Waterman). Q-Gram, Jaro/Winkler, Monge-Elkan, Ext Jaccard Distance, Soft TFIDF, Longest common substring, Bag compression distance, Editext, Syllabe Alignment Distance
Other attributes: Date, Age, Time, Geographical coordinates
Record vector comparison
### 4- Classification
Threshold based, probabilistic, cost-based, rule-based
Supervised: Decision Tree, SVM, Active Learning
### 5- Evaluation
Accuracy, Precision, Recall, F-measure, Specificity, False Positive Rate, ROC curve

## Additional Reference Literature

* Parallel Entity Resolution with Dedoop – Lars Kolb, Erhard Rahm. Institut fur Informatik, Universitat Leipzig, Germany, 2013
* Efficient Parallel Set-Similarity Joins using MapReduce. Rares Vernica, Michael J. Carey, Chen Li. Dept of Computer Science, University of California, Irvine. USA. 2010
* An efficient spark-based adaptive windowing for entity matching. Data Quality Research Group, Federal University of Campina Grande, Paraiba Brazil. 2016
* Data Partitioning for Parallel Entity Matching. Toralf Kirsten and others. Dept. of Computer Science, University of Leipzig, Germany. 2010
* Learning Blocking Schemes for Record Linkage. Matthew Michelson and Craig A. Konblock. University of Southern California. 2006.
* Multi-Relational Record Linkage – Parag and Pedro Domingos. Dept of Computer Science and Engineering, University of Washington, USA
* A Bayesian approach to Graphical Record Linkage and De-duplication. Rebecca C. Steorts, Rob Hall and Stephen E. Fienberg. Dept. of Statistical Science, Duke University, Durham,NC, USA. 2015
* Febrl - A Parallel Open Source Data Linkage System, Peter Christen, Tim Churches and Markus Hegland. Proceedings of the 8th Pacific-Asia Conference, PAKDD 2004, Sydney, Australia, May 26-28, 2004. Pages 638 - 647. Springer Lecture Notes in Artificial Intelligence, Volume 3056.









