provider "aws" {
  region = "eu-west-1"
}

data "template_file" "bootstrap" {
  template = "${file("boot.tlp")}"
  vars = {
    DATAPOINT_KEY="${var.DATAPOINT_KEY}"
    WEATHERSPARK_C_TOKEN="${var.WEATHERSPARK_C_TOKEN}"
    WEATHERSPARK_C_SECRET="${var.WEATHERSPARK_C_SECRET}"
    WEATHERSPARK_A_TOKEN="${var.WEATHERSPARK_A_TOKEN}"
    WEATHERSPARK_A_SECRET="${var.WEATHERSPARK_A_SECRET}"
  }
}


resource "aws_instance" "theosparkline" {
  ami                   = "ami-d41d58a7"
  instance_type         = "t2.micro"
  key_name              = "gateway"
  user_data             = "${data.template_file.bootstrap.rendered}"
  tags {
    Name = "tech-connect-games"
  }
}
