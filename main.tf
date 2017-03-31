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
}
