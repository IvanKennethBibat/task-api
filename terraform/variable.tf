variable "aws_region" {
    description = "AWS Region Specification"
    type = string
    default = "eu-north-1"
}

variable "vpc_cidr" {
    description = "IP Address Range for the VPC (max 65536)"
    type = string
    default = "10.0.0.0/16"
}