Data Analysis of [jimmy-1-step-like-partial](../../data/jimmy-1-step-like)
========================================================

## Read Data

```r
# Read data of which users like what media.
likes <- read.csv("../../data/jimmy-1-step-like")
```


## Check Duplication

```r
# 0 means no duplication; otherwise duplication exists.
anyDuplicated(likes)
```

```
## [1] 0
```


## General Information

```r
# Number of likes
num_likes <- nrow(likes)
num_likes
```

```
## [1] 6645
```

```r
# Number of unique users
num_users <- length(unique(likes$user))
num_users
```

```
## [1] 1400
```

```r
# Number of unique media
num_media <- length(unique(likes$medium))
num_media
```

```
## [1] 1181
```

```r
# Sparsity of the utility matrix (% of known entries)
(num_likes/num_users/num_media) * 100
```

```
## [1] 0.4019
```


## Analyze Like Distribution
### User-Based

```r
# Count number of likes for each user.
user_like_count <- data.frame(table(likes$user))$Freq
# Display summary of number of likes for each user.
summary(user_like_count)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##    1.00    1.00    2.00    4.75    5.00   82.00
```

```r
# Only includes counts > 20 to make histogram concise.
user_like_count_lt20 <- user_like_count[user_like_count < 20]
# Get histogram object.
h <- hist(user_like_count_lt20,
          breaks=seq(0, 20),
          plot=FALSE)

# Change density to percentage.
h$density <- (h$counts / num_users) * 100

# Plot histogram (with counts on top of bars).
plot(h, freq=FALSE, labels=paste(h$counts),
     main="Histogram of user_like_count < 20",
     xlab="Number of likes",
     ylab="Percentage of users (%)")
```

![plot of chunk UserLikeDistribution](figure/UserLikeDistribution1.png) 

```r
# Plot number of user's likes.
plot(sort(user_like_count, decreasing=TRUE),
     main="Number of user's likes",
     xlab="User index",
     ylab="Number of likes")
```

![plot of chunk UserLikeDistribution](figure/UserLikeDistribution2.png) 


### Medium-Based

```r
# Count number of likes for each medium.
medium_like_count <- data.frame(table(likes$medium))$Freq

# Display summary of number of likes for each medium.
summary(medium_like_count)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##    1.00    2.00    4.00    5.63    8.00   43.00
```

```r
# Get histogram object.
h <- hist(medium_like_count,
          plot=FALSE)

# Change density to percentage.
h$density <- (h$counts / num_media) * 100

# Plot histogram (with counts on top of bars).
plot(h, freq=FALSE, labels=paste(h$counts),
     xlab="Number of likes",
     ylab="Percentage of media (%)")
```

![plot of chunk MediumLikeDistribution](figure/MediumLikeDistribution1.png) 

```r
# Plot number of medium's likes
plot(sort(medium_like_count, decreasing=TRUE),
     main="Number of medium's likes",
     xlab="Medium index",
     ylab="Number of likes")
```

![plot of chunk MediumLikeDistribution](figure/MediumLikeDistribution2.png) 

