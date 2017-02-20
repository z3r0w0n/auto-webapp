output "ip" {
    value = ["${join(",", aws_instance.demovm.*.public_ip)}"]
}
