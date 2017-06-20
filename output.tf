output "conn4" {
  value = "http://${aws_instance.techconnectgames.public_ip}:3000/conn4"
}

output "xAndOs" {
  value = "http://${aws_instance.techconnectgames.public_ip}:3000/xandos"
}
