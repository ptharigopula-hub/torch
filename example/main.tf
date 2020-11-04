# Configure the MySQL provider
terraform {
  required_providers {
    mysql = {
      source  = "terraform-providers/mysql"
      version = ">= 1.5"
    }
  }
}

provider "mysql" {
  endpoint = "${var.cluster_endpoint}"
  username = var.master_username
  password = var.master_password
}

resource "mysql_user" "db_user" {
  user               = var.db_username
  plaintext_password = var.db_userpassword
}
