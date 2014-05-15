Data Analysis of `user-like-medium.csv`
========================================================

## Read Data

```r
# Read data of which users like what media.
likes <- read.csv("../data/user-like-medium.csv")
```


## Check Duplication

```r
# 0 means no duplication; otherwise duplication exists.
anyDuplicated(likes)
```

```
## [1] 0
```


## Preprocess Data

```r
# Remove '_' from medium ID (so we can use rle() later)
likes$medium <- gsub("_", "", likes$medium)
```


## General Information

```r
# Number of likes
num_likes <- nrow(likes)
num_likes
```

```
## [1] 1292502
```

```r
# Number of unique users
num_users <- length(unique(likes$user))
num_users
```

```
## [1] 208468
```

```r
# Number of unique media
num_media <- length(unique(likes$medium))
num_media
```

```
## [1] 25105
```


## Analyze Like Distribution
### User-Based

```r
# Count number of likes for each user.
user_like_count <- rle(sort(likes$user))$lengths
# Display summary of number of likes for each user.
summary(user_like_count)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##     1.0     1.0     2.0     6.2     4.0  1550.0
```

```r
# Draw histogram:
#   - x: number of likes
#   - y: number of users
user_like_count_lt20 <- user_like_count[user_like_count < 20]
histogram <- hist(user_like_count_lt20,
                  breaks=seq(0, 20),
                  main="Histogram of user_like_count < 20",
                  xlab="Number of likes",
                  ylab="Number of users")
```

![plot of chunk UserLikeDistribution](figure/UserLikeDistribution.png) 

```r
histogram$breaks
```

```
##  [1]  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
```

```r
histogram$counts
```

```
##  [1] 103042  31936  16667  10342   7124   5239   4025   3052   2570   2224
## [11]   1798   1586   1266   1185   1087    888    834    733    669      0
```

```r
# Percentage
100 * histogram$counts / num_users
```

```
##  [1] 49.4282 15.3194  7.9950  4.9610  3.4173  2.5131  1.9308  1.4640
##  [9]  1.2328  1.0668  0.8625  0.7608  0.6073  0.5684  0.5214  0.4260
## [17]  0.4001  0.3516  0.3209  0.0000
```


### Medium-Based

```r
# Count number of likes for each medium.
medium_like_count <- rle(sort(likes$medium))$lengths
# Display summary of number of likes for each medium.
summary(medium_like_count)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##     1.0     7.0    21.0    51.5   115.0   120.0
```

```r
# Draw histogram:
#   - x: number of likes
#   - y: number of media
histogram <- hist(medium_like_count,
                  xlab="Number of likes",
                  ylab="Number of media")
```

![plot of chunk MediumLikeDistribution](figure/MediumLikeDistribution.png) 

```r
histogram$breaks
```

```
##  [1]   0  10  20  30  40  50  60  70  80  90 100 110 120
```

```r
histogram$counts
```

```
##  [1] 8581 3811 1355  860  580  387  275  193  187  154  509 8213
```

```r
# Percentage
100 * histogram$counts / num_media
```

```
##  [1] 34.1804 15.1802  5.3973  3.4256  2.3103  1.5415  1.0954  0.7688
##  [9]  0.7449  0.6134  2.0275 32.7146
```

