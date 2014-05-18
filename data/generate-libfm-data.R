# Read data.
likes <- read.csv("user-like-medium.csv")

# Append rating column for libfm.
likes[, "Rating"] <- 1

# Calculate range of sub-train, validation, and test set.
# Percentage: sub-train (60%); val (20%); test (20%).
num_likes <- nrow(likes)
num_subtrain <- floor(num_likes * 0.6)
num_val <- floor(num_likes * 0.2)
num_test <- num_likes - num_subtrain - num_val
subtrain_range <- 1:num_subtrain
val_range <- (num_subtrain + 1):(num_subtrain + num_val)
test_range <- (num_subtrain + num_val + 1):num_likes

# Write data.
write.table(likes[subtrain_range,],
            file="subtrain",
            row.names=FALSE,
            col.names=FALSE,
            sep=" ",
            quote=FALSE)
write.table(likes[val_range,],
            file="val",
            row.names=FALSE,
            col.names=FALSE,
            sep=" ",
            quote=FALSE)
write.table(likes[test_range,],
            file="test",
            row.names=FALSE,
            col.names=FALSE,
            sep=" ",
            quote=FALSE)