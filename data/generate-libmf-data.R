# Record start execution time.
start <- proc.time()

# Read data.
likes <- read.csv("user-like-medium.csv")

# Map raw user and item ID to positive integers for libmf.
## Convert factor to numeric.
users <- as.numeric(factor(likes$user))
media <- as.numeric(likes$medium)

# Rating column.
ratings <- rep(1, nrow(likes))

# Replace raw data with transformed data.
likes <- data.frame(user=users,
                    medium=media,
                    rating=ratings)

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
outputs <- list(
  list(data=likes[subtrain_range,], file="libmf/subtrain"),
  list(data=likes[val_range,], file="libmf/val"),
  list(data=likes[test_range,], file="libmf/test"))
for (output in outputs)
{
  write.table(output$data,
              file=output$file,
              row.names=FALSE,
              col.names=FALSE,
              sep=" ",
              quote=FALSE)
}

# Record end execution time.
end <- proc.time()

# Print execution time.
cat("[Time Spent]\n")
print(end - start)