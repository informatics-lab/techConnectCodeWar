provider "aws" {
  region = "eu-west-1"
}

data "template_file" "bootstrap" {
  template = "${file("boot.tlp")}"
}


resource "aws_instance" "techconnectgames" {
  ami                   = "ami-d41d58a7"
  instance_type         = "t2.micro"
  key_name              = "gateway"
  user_data             = "${data.template_file.bootstrap.rendered}"
  tags {
    Name = "tech-connect-games"
  }
  security_groups        = ["default", "${aws_security_group.security_techconnectgames.name}"]
}


resource "aws_security_group" "security_techconnectgames" {
  name = "security_techconnectgames"
  description = "Allow web traffic to techconnectgames"

  ingress {
      from_port = 3000
      to_port = 3000
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }
}
