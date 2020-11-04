variable "cluster_endpoint" {
  description = "The aurora db cluster endpoint."
  type        = string
}

variable "master_username" {
  description = "The username for the master user. Required unless this is a secondary database in a global Aurora cluster."
  type        = string
  default     = "admin"
}

variable "master_password" {
  description = "The password for the master user. Required unless this is a secondary database in a global Aurora cluster. If var.snapshot_identifier is non-empty, this value is ignored."
  type        = string
  default     = "something"
}

variable "db_username" {
  description = "The username for database user. Required if user is getting created on aurora mysql db cluster."
  type        = string
}


variable "db_userpassword" {
  description = "The password for database user. Required if user is getting created on aurora mysql db cluster."
  type        = string
}
