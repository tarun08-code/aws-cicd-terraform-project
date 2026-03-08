variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-1"
}

variable "key_name" {
  description = "Name of your EC2 key pair"
  default     = "Devops"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.micro"
}
