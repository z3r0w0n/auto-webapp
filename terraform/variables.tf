variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "us-west-2"
}

# Ubuntu Precise 12.04 LTS (x64)
variable "aws_amis" {
  default = {
    eu-west-1 = "ami-b1cf19c6"
    us-east-1 = "ami-de7ab6b6"
    us-west-1 = "ami-3f75767a"

    us-west-2 = "ami-d2c924b2"
  }
}

variable "clustername" {}
variable "instance_count" {}
variable "instance_type" {}
variable "key_name" {
  default = "demokp"
}
variable "ssh_user" {}
