output "instance_public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_eip.app_eip.public_ip
}

output "instance_id" {
  description = "ID of EC2 instance"
  value       = aws_instance.app_server.id
}

output "ssh_command" {
  description = "Command to SSH into instance"
  value       = "ssh -i devops.pem ec2-user@${aws_eip.app_eip.public_ip}"
}

output "jenkins_url" {
  description = "Jenkins dashboard URL"
  value       = "http://${aws_eip.app_eip.public_ip}:8080"
}

output "app_url" {
  description = "Application URL"
  value       = "http://${aws_eip.app_eip.public_ip}:5000"
}
