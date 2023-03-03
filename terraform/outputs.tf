
output "distribution_domain_name" {
  description = "ID of the EC2 instance"
  value       = aws_cloudfront_distribution.s3_distribution.domain_name
}